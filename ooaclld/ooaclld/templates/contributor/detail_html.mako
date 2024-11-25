<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "contributors" %>
<%block name="title">${ctx.name}</%block>
<% has_authorship = False %>
<% has_contributor = False %>
% for c in ctx.contribution_assocs:
	% if c.primary:
	    <% has_authorship = True %>
    % else:
        <% has_contributor = True %>
    % endif
%endfor

<h2>${ctx.name}

% if ctx.jsondatadict.get("orcid", None):
<a href="https://orcid.org/${ctx.jsondatadict["orcid"]}"><img style="height:.8em" src="${request.static_url('clld:web/static/images/orcid.svg')}" /></a>


% endif
</h2>
% if ctx.description:
<p>${ctx.description}</p>
% endif

<dl>
    % if ctx.address:
    <dt>${_('Address')}:</dt>
    <dd>
        <address>
            ${h.text2html(ctx.address)|n}
        </address>
    </dd>
    % endif
    % if ctx.url:
    <dt>${_('Web:')}</dt>
    <dd>${h.external_link(ctx.url)}</dd>
    % endif
    % if ctx.email:
    <dt>${_('Mail:')}</dt>
    <dd>${ctx.email.replace('@', '[at]')}</dd>
    % endif
    ${util.data(ctx, with_dl=False)}
</dl>

<ul>
% if has_authorship:
<h3>Author:</h3>
    <ul>
    % for c in ctx.contribution_assocs:
        % if c.primary:
            <li>${h.link(request, c.contribution)}</li>
        % endif
    % endfor
    </ul>
    <br/>
% endif
% if has_contributor:
<h3>Contributor:</h3>
    <ul>
    % for c in ctx.contribution_assocs:
        % if not c.primary:
            <li>${h.link(request, c.contribution)}</li>
        % endif
    % endfor
    </ul>
</ul>
% endif