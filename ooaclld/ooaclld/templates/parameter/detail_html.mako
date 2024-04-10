<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "parameters" %>
<%! from ooaclld.models import OOAValue %>
<% values_dt = request.get_datatable('values', OOAValue, parameter=ctx) %>
<%block name="title">${_('Feature')} ${ctx.name}</%block>


<div class="row-fluid">
    <div class="span8">
        <h1>${ctx.id}</h1>

        ## clld.web.util.helpers alt_representation creates download widget with info button
        <div>${h.alt_representations(req, ctx, doc_position='right', exclude=['snippet.html'])|n}</div>
        % if ctx.question:
        <h2>${ctx.question}</h2>
        % endif
        <p>
            This feature is described in the feature set 
            <a href="${request.resource_url(ctx.featureset)}">${ctx.featureset}</a>.
        </p>
        <p> 
            It is authored by ${h.linked_contributors(request, ctx.featureset)}.
            ${h.cite_button(request, ctx.featureset)}
        </p>
    </div>
    <p></p>
    <div class="span4">
        <%util:well title="Values">
            ${u.value_table(ctx, request)}
        </%util:well>
    </div>
</div>
${request.get_map('parameter', dt=values_dt).render()}
${values_dt.render()}




