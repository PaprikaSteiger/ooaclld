import itertools

from clld.web.util.htmllib import HTML, literal
from clld.web.util.helpers import map_marker_img, get_adapter, external_link
from clld.db.meta import DBSession
from clld.db.models import common
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
    # if ctx.multivalued:
    parts.append(HTML.thead(
        HTML.tr(*[HTML.th(s, class_='right')
                  for s in [' ', '             ', 'exclusive', 'partial', 'all']]))
    )
    parts.append(HTML.tbody(*rows))
    return HTML.table(*parts, class_='table table-condensed')


def parameter_link(req, sym, p):
    return HTML.a(sym, href=req.resource_url(p), style="color: black;") if p else sym