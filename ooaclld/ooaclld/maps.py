from clld.web.maps import ParameterMap, Map, Layer, CombinationMap
from clld.web.util.helpers import JS, map_marker_img


class FeatureMap(ParameterMap):
    def get_options(self):
        return {
            "icon_size": 20,
            "max_zoom": 9,
            "worldCopyJump": True,
            "zoom": 5,
            #'on_init': JS('wals_parameter_map_on_init'),
            "info_query": {"parameter": self.ctx.pk},
        }


def includeme(config):
    config.register_map("parameter", ParameterMap)
