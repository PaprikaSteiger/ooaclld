from collections import Counter

from clld.interfaces import IValueSet, IValue, IDomainElement
from clld.web.icon import MapMarker
from clldutils import svg
from clld.interfaces import IIcon

class OaaMapMarker(MapMarker):
    @staticmethod
    def pie(*slices):
        return svg.data_url(svg.pie(
            [float(p[0]) for p in slices],
            [p[1] for p in slices],
            stroke_circle=False))

    def __call__(self, ctx, req):
        #if IValueSet.providedBy(ctx):
        if IDomainElement.providedBy(ctx):
            # if req.matched_route.name == 'valueset' and not ctx.parameter.multivalued:
            #     return self.pie((100, ctx.values[0].domainelement.jsondata['color']))
            slices = Counter()
            # for v in ctx.values:
            #
            #len(ctx.values)
            icon = ctx.jsondata['icon']
            if icon and icon.startswith("#"):
                for value in ctx.values:
                    slices[icon] += value.frequency or 1

                return self.pie(*[(v, k) for k, v in slices.most_common()])

        if IValueSet.providedBy(ctx):
            slices = Counter()
            for value in ctx.values:
                icon = value.domainelement.jsondata['icon']
                if icon and icon.startswith("#"):
                    slices[icon] += value.frequency or 1
            return self.pie(*[(v, k) for k, v in slices.most_common()])

        if IValue.providedBy(ctx):
            slices = Counter()
            for value in ctx.values:
                icon = value.domainelement.jsondata['icon']
                if icon and icon.startswith("#"):
                    slices[icon] += value.frequency or 1
            return self.pie(*[(v, k) for k, v in slices.most_common()])

        return super(OaaMapMarker, self).__call__(ctx, req)