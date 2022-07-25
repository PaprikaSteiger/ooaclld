<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "parameters" %>
<%block name="title">${_('Parameter')} ${ctx.name}</%block>
<%! from ooaclld.models import OOAParameter %>



<h2>Feature Set: ${ctx.name}</h2>

<div style="clear: both"/>
${request.get_datatable('parameters',OOAParameter, ooafeatureset=ctx).get_query().first()}
${request.get_datatable('parameters',OOAParameter, ooafeatureset=ctx).render()}
