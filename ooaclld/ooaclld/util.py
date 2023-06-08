from clld.web.util.htmllib import HTML, literal
from clld.web.util.helpers import map_marker_img, get_adapter, external_link


def contribution_detail_html(context=None, request=None, **kw):
    c = context.description
    if c and "<body>" in c:
        c = c.split("<body>")[1].split("</body>")[0]
    return {"text": c}


def value_table(ctx, req):
    rows = []
    langs = {}

    for i, de in enumerate(ctx.domain):
        exclusive = 0
        shared = 0

        for v in [_v for _v in de.values]:

            if len(v.valueset.values) > 1:
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
        HTML.td('Representation:', colspan=str(len(cells) - 1), class_='right'),
        HTML.td('%s' % len(langs), class_='right')))

    parts = []
    # if ctx.multivalued:
    parts.append(HTML.thead(
        HTML.tr(*[HTML.th(s, class_='right')
                  for s in [' ', '             ', 'excl', 'shrd', 'all']]))
    )
    parts.append(HTML.tbody(*rows))
    return HTML.table(*parts, class_='table table-condensed')


def parameter_link(req, sym, p):
    return HTML.a(sym, href=req.resource_url(p), style="color: black;") if p else sym