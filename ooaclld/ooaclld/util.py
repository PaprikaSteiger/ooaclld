import itertools
import typing

from clld.web.util.htmllib import HTML, literal
from clld.web.util.helpers import map_marker_img, get_adapter, external_link
from clld.db.meta import DBSession
from clld.db.models import common
from clldutils.color import rgb_as_hex
from clldutils.svg import svg
from sqlalchemy.orm import joinedload


def contribution_detail_html(context=None, request=None, **kw):
    c = context.description
    if c and "<body>" in c:
        c = c.split("<body>")[1].split("</body>")[0]
    return {"text": c}


def value_table(ctx, req):
    rows = []
    langs = {}

    domain = {de.pk: de for de in ctx.domain}
    q = DBSession.query(common.Value)\
        .filter(common.Value.domainelement_pk.in_(list(domain)))\
        .order_by(common.Value.domainelement_pk, common.Value.valueset_pk)\
        .options(joinedload(common.Value.valueset)).all()
    vspks = [v.valueset_pk for v in q]

    for depk, vals in itertools.groupby(q, lambda v: v.domainelement_pk):
        de = domain[depk]
        exclusive = 0
        shared = 0
        icon = de.jsondata['icon']
        if not icon:
            continue
        for v in vals:
            if vspks.count(v.valueset_pk) > 1:
                shared += 1
            else:
                exclusive += 1
            langs[v.valueset.language_pk] = 1

        cells = [
            HTML.td(map_marker_img(req, de)),
            HTML.td(literal(de.description)),
            HTML.td(str(exclusive), class_='right'),
        ]
        cells.append(HTML.td(str(shared), class_='right'))
        cells.append(HTML.td(str(len(de.values)), class_='right'))
        rows.append(HTML.tr(*cells))


    rows.append(HTML.tr(
        HTML.td('Total Languages:', colspan=str(len(cells) - 1), class_='right'),
        HTML.td('%s' % len(langs), class_='right')))

    parts = []
    parts.append(HTML.thead(
        HTML.tr(*[HTML.th(s, class_='right')
                  for s in [' ', '             ', 'exclusive', 'partial', 'all']]))
    )
    parts.append(HTML.tbody(*rows))
    return HTML.table(*parts, class_='table table-condensed')


def parameter_link(req, sym, p):
    return HTML.a(sym, href=req.resource_url(p), style="color: black;") if p else sym

# unique pie() function for ATLAs, incorporating opacity
def ATLAsPie(data: typing.List[typing.Union[float, int]],
             colors: typing.Optional[typing.List[str]] = None,
             titles: typing.Optional[typing.List[str]] = None,
             width: int = 34,
             stroke_circle: bool = False,
             opacity: float = 1) -> str:
    """
    An SVG pie chart.

    :param data: list of numbers specifying the proportional sizes of the slices.
    :param colors: list of RGB colors as hex triplets, specifying the respective colors of the \
    slices.
    :param titles: list of strings to use as titles for the respective slices.
    :param width: Width of the SVG object.
    :param stroke_circle: Whether to stroke (aka outline) theboundary of the pie.
    :return: SVG XML representation of the data as pie chart.
    """
    colors = clldutils.color.qualitative_colors(len(data)) if colors is None else colors
    assert len(data) == len(colors)
    zipped = [(d, c) for d, c in zip(data, colors) if d != 0]
    data, colors = [z[0] for z in zipped], [z[1] for z in zipped]
    cx = cy = round(width / 2, 1)
    radius = round((width - 2) / 2, 1)
    current_angle_rad = 0
    svg_content = []
    total = sum(data)
    titles = titles or [None] * len(data)
    stroke_circle = 'black' if stroke_circle is True else stroke_circle or 'none'

    def endpoint(angle_rad):
        """
        Calculate position of point on circle given an angle, a radius, and the location
        of the center of the circle Zero line points west.
        """
        return (round(cx - (radius * math.cos(angle_rad)), 1),
                round(cy - (radius * math.sin(angle_rad)), 1))

    if len(data) == 1:
        svg_content.append(
            '<circle cx="{0}" cy="{1}" r="{2}" style="stroke:{3}; fill:{4}; fill-opacity:{5}">'.format(
                cx, cy, radius, stroke_circle, rgb_as_hex(colors[0]), opacity))
        if titles[0]:
            svg_content.append('<title>{0}</title>'.format(escape(titles[0])))
        svg_content.append('</circle>')
        return svg(''.join(svg_content), height=width, width=width)

    for angle_deg, color, title in zip([360.0 / total * d for d in data], colors, titles):
        radius1 = "M{0},{1} L{2},{3}".format(cx, cy, *endpoint(current_angle_rad))
        current_angle_rad += math.radians(angle_deg)
        arc = "A{0},{1} 0 {2},1 {3} {4}".format(
            radius, radius, 1 if angle_deg > 180 else 0, *endpoint(current_angle_rad))
        radius2 = "L%s,%s" % (cx, cy)
        svg_content.append(
            '<path d="{0} {1} {2}" style="{3}" transform="rotate(90 {4} {5})">'.format(
                radius1, arc, radius2, style(fill=rgb_as_hex(color)), cx, cy))
        if title:
            svg_content.append('<title>{0}</title>'.format(escape(title)))
        svg_content.append('</path>')

    if stroke_circle != 'none':
        svg_content.append(
            '<circle cx="%s" cy="%s" r="%s" style="stroke:%s; fill:none;"/>'
            % (cx, cy, radius, stroke_circle))

    return svg(''.join(svg_content), height=width, width=width)