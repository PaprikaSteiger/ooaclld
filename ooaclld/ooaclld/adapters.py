from clld import interfaces
from clld.web.adapters import GeoJsonParameter
from clld.db.meta import DBSession
from clld.db.models import common
from clldutils.svg import pie, data_url
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
        if valueset.parameter.id == 'Cor-02':
            val = valueset.values[0]
            if val.domainelement and val.domainelement.jsondata.get('icon'):
                res['icon'] = data_url(pie([1], [val.domainelement.jsondata['icon']], width=5*int(val.value or 0)))
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
