<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "references" %>
<%block name="title">${_('References')}</%block>

<h2>${_('References')}</h2>
<div>
    ${ctx.render()}
</div>