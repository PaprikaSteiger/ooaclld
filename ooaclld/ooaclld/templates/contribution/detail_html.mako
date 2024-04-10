<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "featuresets" %>
<%block name="title">${ctx.name}</%block>
<%! from ooaclld.models import OOAParameter %>
<style>
h3 { padding-top: 25px; }
</style>


<h1>${ctx.name}</h1>
% if text:
    <%! from clld_markdown_plugin import markdown %>
    ${markdown(req, text)|n}
% else:
    No static page available
% endif
<div style="clear: both"/>

