# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1490087534.5503628
_enable_loop = True
_template_filename = '/home/aleph/PROG/PIT/nikola/lib/python3.5/site-packages/nikola/data/themes/sdll/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'sourcelink', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def content():
            return render_content(context._locals(__M_locals))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def content():
            return render_content(context)
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if title:
            __M_writer('    <h1>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        if post:
            __M_writer('    <p>\n        ')
            __M_writer(str(post.text()))
            __M_writer('\n    </p>\n')
        if folders:
            __M_writer('    <ol>\n')
            for folder, ftitle in folders:
                __M_writer('        <li><a href="')
                __M_writer(str(folder))
                __M_writer('"><i\n        class="icon-folder-open"></i>&nbsp;')
                __M_writer(filters.html_escape(str(ftitle)))
                __M_writer('</a></li>\n')
            __M_writer('    </ol>\n')
        if photo_array:
            __M_writer('    <ul class="thumbnails">\n')
            for image in photo_array:
                __M_writer('            <li><a href="')
                __M_writer(str(image['url']))
                __M_writer('" class="thumbnail image-reference" title="')
                __M_writer(str(image['title']))
                __M_writer('">\n                <img src="')
                __M_writer(str(image['url_thumb']))
                __M_writer('" alt="')
                __M_writer(filters.html_escape(str(image['title'])))
                __M_writer('" /></a>\n')
            __M_writer('    </ul>\n')
        if site_has_comments and enable_comments:
            __M_writer('    ')
            __M_writer(str(comments.comment_form(None, permalink, title)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "gallery.tmpl", "filename": "/home/aleph/PROG/PIT/nikola/lib/python3.5/site-packages/nikola/data/themes/sdll/templates/gallery.tmpl", "line_map": {"133": 5, "146": 37, "23": 4, "26": 3, "155": 37, "156": 38, "157": 38, "32": 0, "163": 157, "54": 2, "55": 3, "56": 4, "61": 5, "66": 35, "71": 40, "77": 7, "93": 7, "94": 8, "95": 9, "96": 9, "97": 9, "98": 11, "99": 12, "100": 13, "101": 13, "102": 16, "103": 17, "104": 18, "105": 19, "106": 19, "107": 19, "108": 20, "109": 20, "110": 22, "111": 24, "112": 25, "113": 26, "114": 27, "115": 27, "116": 27, "117": 27, "118": 27, "119": 28, "120": 28, "121": 28, "122": 28, "123": 30, "124": 32, "125": 33, "126": 33, "127": 33}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
