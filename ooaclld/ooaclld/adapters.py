from clld import interfaces
from clld.web.adapters import GeoJsonParameter
from clld.db.meta import DBSession
from clld.db.models import common
from clldutils.svg import data_url, style
from ooaclld.util import ATLAsPie
from sqlalchemy.orm import joinedload


class GeoJsonFeature(GeoJsonParameter):
    def feature_iterator(self, ctx, req):
        for vs in DBSession.query(common.ValueSet).filter(common.ValueSet.parameter_pk == ctx.pk).options(
                #joinedload(common.ValueSet.values),
                joinedload(common.ValueSet.language)):
            yield vs

    def feature_properties(self, ctx, req, valueset):
        res = {
            'values': list(valueset.values),
            'label': valueset.language.name}
        if valueset.parameter.datatype == 'integer':
            #print(set([x.values[0] for x in ctx.valuesets]))
            #print(ctx.valuesets[1].values[0].value)
            vals = sorted(set([vs.values[0].value for vs in ctx.valuesets if vs.values[0].value is not None]))
            min_val = 2.7
            scale_factor = 8 / len(vals)
            size_dict = dict()
            for i in range(0, len(vals)):
                size_dict[vals[i]] = min_val + scale_factor * i
            val = valueset.values[0]
            if val.domainelement and val.domainelement.jsondata.get('icon'):
                res['icon'] = data_url(ATLAsPie([1], [val.domainelement.jsondata['icon']], width=size_dict[val.value], opacity=0.65))
        return res

    def featurecollection_properties(self, ctx, req):
        marker = req.registry.getUtility(interfaces.IMapMarker)
        res = {
            'name': getattr(ctx, 'name', 'Values'),
            'domain': [
                {'icon': marker(ctx, req), 'id': de.id, 'name': de.name}
                for de in getattr(ctx, 'domain', [])
            ]
        }
        return res
        #TODO: HERE it s decided what is passed to the mapmarker as context

def includeme(config):
    config.register_adapter(GeoJsonFeature, interfaces.IParameter)
