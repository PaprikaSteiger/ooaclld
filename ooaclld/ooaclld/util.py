

def contribution_detail_html(context=None, request=None, **kw):
    c = context.description
    if c and '<body>' in c:
        c = c.split('<body>')[1].split('</body>')[0]
    return {'text': c}
