<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "featuresets" %>
<%! from ooaclld.models import OOAFeatureSet %>
<%block name="title">Feature Sets</%block>
<h2>Feature Sets</h2>
<p>
    Feature sets are collections of typological features that together capture linguistic variation within a typological domain. The typological domain covered, motivation for its inclusion in the database, a full list of associated features, and results of the study are given in each feature set description.
</p>
<div class="clearfix"> </div>
${ctx.render()}
