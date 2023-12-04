<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "featuresets" %>
<%block name="title">Feature Set ${ctx.name}</%block>
<%! from ooaclld.models import OOAParameter %>

<h2>Feature Set: ${ctx.name}</h2>
% if text:
    <%! from clld_markdown_plugin import markdown %>
    ${markdown(req, text)|n}
% else:
    No static page available
% endif
<div style="clear: both"/>

