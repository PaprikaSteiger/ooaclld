<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "features" %>
<%! from ooaclld.models import OOAValue %>
<% values_dt = request.get_datatable('values', OOAValue, parameter=ctx) %>
<%block name="title">${_('Feature')} ${ctx.name}</%block>


<div class="row-fluid">
    <div class="span8">
        <h2>Feature ID: ${ctx.id}</h2>

        ## clld.web.util.helpers alt_representation creates download widget with info button
        <div>${h.alt_representations(req, ctx, doc_position='right', exclude=['snippet.html'])|n}</div>
        % if ctx.question:
        <p>Feature description: ${ctx.question}</p>
        % endif
        <p>
            This feature is described in featureset ${ctx.featureset}
            <a class="button btn" href="${request.resource_url(ctx.featureset)}"/>
            by ${h.linked_contributors(request, ctx.featureset)}
            ${h.cite_button(request, ctx.featureset)}
        </p>

    </div>
    <p></p>
    % if ctx.featureset:
        <div class="span4">
            <%util:well title="Authors">
                <span>${h.linked_contributors(request, ctx.featureset)}</span>
                ${h.cite_button(request, ctx.featureset)}
            </%util:well>
        </div>
    % endif
    <div class="span4">
        <%util:well title="Values">
        <p>Feature description: ${ctx.question}</p>
            ${u.value_table(ctx, request)}
        </%util:well>
    </div>
</div>
${request.get_map('parameter', dt=values_dt).render()}
${values_dt.render()}




