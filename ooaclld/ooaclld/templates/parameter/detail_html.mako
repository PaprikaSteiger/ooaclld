<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "parameters" %>
<%block name="title">${_('Feature')} ${ctx.name}</%block>
<%! from ooaclld.models import OOAValue %>



<h2>Feature ID: ${ctx.id}</h2>

## clld.web.util.helpers alt_representation creates download widget with info button
<div>${h.alt_representations(req, ctx, doc_position='right', exclude=['snippet.html'])|n}</div>
% if ctx.question:
<p>Feature description: ${ctx.question}</p>
% endif
<p>
    This feature is described in featureset ${ctx.featureset}
    <a class="button btn" href="${request.resource_url(ctx.featureset)}"/>
    by ${h.linked_contributors(request, ctx.featureset)}
    ${h.cite_button(request, ctx.featureset)}
</p>

<div style="clear: both"/>
##% if map_ or request.map:
##    ${(map_ or request.map).render()}
##% endif

${request.get_datatable('values', OOAValue, ooaparameter=ctx).render()}

