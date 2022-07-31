<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "featuresets" %>
<%block name="title">Feature Set ${ctx.name}</%block>
<%! from ooaclld.models import OOAParameter %>

<h2>Feature Set: ${ctx.name}</h2>
##${text|n}
${dir(ctx)}
${ctx.contributors}
<div style="clear: both"/>

