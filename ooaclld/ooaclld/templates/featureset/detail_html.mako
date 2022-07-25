<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "parameters" %>
<%block name="title">${_('Parameter')} ${ctx.name}</%block>
<%! from ooaclld.models import OOAParameter %>



<h2>${_('Feature Set')} ${ctx.name}</h2>

% if ctx.description:
<p>${ctx.description}</p>
% endif

<div style="clear: both"/>
% if map_ or request.map:
${(map_ or request.map).render()}
% endif
${dir(request.get_datatable('parameters',OOAParameter, ooafeatureset=ctx))}
${request.get_datatable('parameters',OOAParameter, ooafeatureset=ctx).ooafeatureset}
${request.get_datatable('parameters',OOAParameter, ooafeatureset=ctx).render()}
