<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "languages" %>
<%block name="title">Language ${ctx.name}</%block>
<%! from ooaclld.models import OOAUnit %>


<h2>Language: ${ctx.name}</h2>
<span class="badge">Glotto code: ${ctx.id}</span>
${request.get_datatable('units', OOAUnit, ooalanguage=ctx).render()}

<%def name="sidebar()">
    ${util.codes()}
    <div style="clear: right;"> </div>
    <%util:well>
        ${request.map.render()}
        ${h.format_coordinates(ctx)}
        ## ${util.dl_table(('Spoken in', h.literal(', '.join(h.link(request, c) for c in ctx.countries))))}
    </%util:well>
    % if ctx.sources:
    <%util:well title="Sources">
        ${util.sources_list(sorted(list(ctx.sources), key=lambda s: s.name))}
        <div style="clear: both;"></div>
    </%util:well>
    % endif
</%def>
