<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "featuresets" %>
<%! from ooaclld.models import OOAFeatureSet %>
<%block name="title">Feature Sets</%block>
<h2>Feature Sets</h2>
<p>
    Those are the OOA Feature Sets. INSERT MORE TEXT HERE.
</p>
<div class="clearfix"> </div>
${ctx.render()}
