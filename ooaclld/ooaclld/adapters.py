from clld import interfaces
from clld.web.adapters import GeoJsonParameter


class GeoJsonFeature(GeoJsonParameter):
    def feature_iterator(self, ctx, req):
        for vs in ctx.valuesets:
            yield vs

    def feature_properties(self, ctx, req, valueset):
        return {
            'values': list(valueset.values),
            'label': valueset.language.name}

    def featurecollection_properties(self, ctx, req):
        marker = req.registry.getUtility(interfaces.IMapMarker)
        res = {
            'name': getattr(ctx, 'name', 'Values'),
            'domain': [
                {'icon': marker(ctx, req), 'id': de.id, 'name': de.name}
                for de in getattr(ctx, 'domain', ctx)
            ]
        }
        return res
        #HERE it s decided what is passed to the mapmarker as context

def includeme(config):
    config.register_adapter(GeoJsonFeature, interfaces.IParameter)
