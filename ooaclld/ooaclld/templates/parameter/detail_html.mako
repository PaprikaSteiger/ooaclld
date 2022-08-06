<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "parameters" %>
<%block name="title">${_('Parameter')} ${ctx.name}</%block>
<%! from ooaclld.models import OOAValue %>



<h2>Parameter ${ctx.id}</h2>

% if ctx.description:
<p>${ctx.description}</p>
% endif

<div style="clear: both"/>
% if map_ or request.map:
##${(map_ or request.map).render()}
% endif
${request.get_datatable('values', OOAValue, ooaparameter=ctx).render()}

