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
            ['#' + p[1] for p in slices],
            stroke_circle=True))

    def __call__(self, ctx, req):
        #if IValueSet.providedBy(ctx):
        if IDomainElement.providedBy(ctx):
            breakpoint()
            # if req.matched_route.name == 'valueset' and not ctx.parameter.multivalued:
            #     return self.pie((100, ctx.values[0].domainelement.jsondata['color']))
            slices = Counter()
            # for v in ctx.values:
            #
            #len(ctx.values)
            icon = ctx.domainelement
            for value in ctx.values:
                if value.value == "no":
                    icon = 'ffffff'
                    slices[icon] += value.frequency or 1
                elif value.value == "yes":
                    icon = 'ffff00'
                    slices[icon] += value.frequency or 1
                elif value.value == "1":
                    icon = 'dd0000'
                    slices[icon] += value.frequency or 1
                elif value.value == "2":
                    icon = '990099'
                    slices[icon] += value.frequency or 1
                elif value.value == "3":
                    icon = '00ff00'
                    slices[icon] += value.frequency or 1

            #return svg.data_url(svg.icon(icon))
            print(slices)
            return self.pie(*[(v, k) for k, v in slices.most_common()])

        if IValue.providedBy(ctx):
            # freq = ctx.frequency or 100
            # slices = [(freq, ctx.domainelement.jsondata['color'])]
            # if freq < 100:
            #     slices.append((100 - freq, 'ffffff'))
            # return self.pie(*slices)
            icon ='cffffcc'

            return svg.data_url(svg.icon(icon))

        if IDomainElement.providedBy(ctx):
            #return self.pie((100, ctx.jsondata['color']))
            icon = 'cffff00'
            return svg.data_url(svg.icon(icon))

        return super(OaaMapMarker, self).__call__(ctx, req)