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
            stroke_circle=True))

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
            # only display on map if color code provided
            if not icon:
                return ""
            elif not icon.startswith("#"):
                return ""
            # create pies
            #icon = icon.strip("#")
            for value in ctx.values:
                slices[icon] += value.frequency or 1

            print(slices)
            return self.pie(*[(v, k) for k, v in slices.most_common()])

        if IValueSet.providedBy(ctx):
            slices = Counter()
            breakpoint()
            for value in ctx.values:
                icon = value.domainelement.jsondata['icon']
                if icon:
                    slices[icon] += value.frequency or 1

            return self.pie(*[(v, k) for k, v in slices.most_common()])

        if IValue.providedBy(ctx):
            breakpoint()
            # freq = ctx.frequency or 100
            # slices = [(freq, ctx.domainelement.jsondata['color'])]
            # if freq < 100:
            #     slices.append((100 - freq, 'ffffff'))
            # return self.pie(*slices)
            icon ='cffffcc'

            return svg.data_url(svg.icon(icon))

        # if IDomainElement.providedBy(ctx):
        #     #return self.pie((100, ctx.jsondata['color']))
        #     icon = 'cffff00'
        #     return svg.data_url(svg.icon(icon))
        return super(OaaMapMarker, self).__call__(ctx, req)