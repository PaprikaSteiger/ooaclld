<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "parameters" %>
<%block name="title">Features</%block>
<%! from ooaclld.models import OOAParameter %>
<h2>Features</h2>
<p>
    A feature is a single structural property, and every feature belongs to some feature set capturing a particular typological domain. Each feature is coded for the entire ATLAs language sample, and may be single-valued, multi-valued, or give frequency information.
</p>
<div class="clearfix"> </div>
${ctx.render()}
