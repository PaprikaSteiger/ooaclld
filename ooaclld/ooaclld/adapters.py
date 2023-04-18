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

def includeme(config):
    config.register_adapter(GeoJsonFeature, interfaces.IParameter)
