<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "parameters" %>
<%block name="title">Features</%block>
<%! from ooaclld.models import OOAParameter %>
<h2>Features</h2>
<p>
    Those are the OOA parameters
    Testing that the other fields aren't empty:
    ${[v.question for v in h.DBSession.query(OOAParameter).all()]}
</p>
${type(ctx)}
<div class="clearfix"> </div>
${ctx.render()}
