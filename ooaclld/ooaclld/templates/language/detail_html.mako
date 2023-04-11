<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "languages" %>
<%block name="title">Language ${ctx.name}</%block>
<%! from ooaclld.models import OOAValue %>


<h2>Language: ${ctx.name}</h2>
${request.get_datatable('values', OOAValue, ooalanguage=ctx).render()}
${util.codes}
<%def name="sidebar()">
    <a href="https://glottolog.org/resource/languoid/id/${ctx.id}"><span class="badge">Glotto code: ${ctx.id}</span></a>
    <div style="clear: right;"> </div>
    <%util:well title="Map">
        ${request.map.render()}
        ${h.format_coordinates(ctx)}
    </%util:well>

    <%util:well title="Sources">
        ${util.sources_list(sorted(list(ctx.sources), key=lambda s: s.name))}
        <div style="clear: both;"></div>
    </%util:well>
</%def>
