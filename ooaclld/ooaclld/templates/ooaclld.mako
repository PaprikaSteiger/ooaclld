<%inherit file="app.mako"/>

##
## define app-level blocks:
##
<%block name="header">
    <div id="header" class="container-fluid">
        <a href="${request.route_url('dataset')}" id="banner-img">
            <img src=${request.static_url('ooaclld:static/banner.png')} />
        </a>
    </div>
</%block>

${next.body()}
