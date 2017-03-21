# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1490087534.7559679
_enable_loop = True
_template_filename = '/home/aleph/PROG/PIT/nikola/lib/python3.5/site-packages/nikola/data/themes/sdll/templates/tag.tmpl'
_template_uri = 'tag.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        kind = context.get('kind', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        translations = context.get('translations', UNDEFINED)
        description = context.get('description', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        title = context.get('title', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        sorted = context.get('sorted', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        description = context.get('description', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        subcategories = context.get('subcategories', UNDEFINED)
        title = context.get('title', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="tagpage">\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n')
        if description:
            __M_writer('        <p>')
            __M_writer(str(description))
            __M_writer('</p>\n')
        if subcategories:
            __M_writer('        ')
            __M_writer(str(messages('Subcategories:')))
            __M_writer('\n        <ul>\n')
            for name, link in subcategories:
                __M_writer('            <li><a href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('        <div class="metadata">\n')
        if len(translations) > 1 and generate_rss:
            for language in sorted(translations):
                __M_writer('                <p class="feedlink">\n                    <a href="')
                __M_writer(str(_link(kind + "_rss", tag, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="application/rss+xml">RSS</a>&nbsp;\n                </p>\n')
        elif generate_rss:
            __M_writer('                <p class="feedlink"><a href="')
            __M_writer(str(_link(kind + "_rss", tag)))
            __M_writer('" type="application/rss+xml">RSS</a></p>\n')
        __M_writer('        </div>\n    </header>\n')
        if posts:
            __M_writer('    <ul class="postlist">\n')
            for post in posts:
                __M_writer('        <li><time class="published dt-published" datetime="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('" title="')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('</time><a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="listtitle"> ')
                __M_writer(str(post.title()))
                __M_writer('<a></li>\n')
            __M_writer('    </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        kind = context.get('kind', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if len(translations) > 1 and generate_rss:
            for language in sorted(translations):
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS for ')
                __M_writer(str(kind))
                __M_writer(' ')
                __M_writer(filters.html_escape(str(tag)))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')" href="')
                __M_writer(str(_link(kind + "_rss", tag, language)))
                __M_writer('">\n')
        elif generate_rss:
            __M_writer('        <link rel="alternate" type="application/rss+xml" title="RSS for ')
            __M_writer(str(kind))
            __M_writer(' ')
            __M_writer(filters.html_escape(str(tag)))
            __M_writer('" href="')
            __M_writer(str(_link(kind + "_rss", tag)))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "tag.tmpl", "filename": "/home/aleph/PROG/PIT/nikola/lib/python3.5/site-packages/nikola/data/themes/sdll/templates/tag.tmpl", "line_map": {"128": 46, "129": 46, "130": 48, "131": 50, "137": 4, "151": 4, "152": 5, "153": 5, "154": 6, "27": 0, "156": 8, "157": 8, "158": 8, "159": 8, "160": 8, "161": 8, "162": 8, "155": 7, "164": 8, "165": 10, "166": 11, "167": 11, "168": 11, "169": 11, "170": 11, "171": 11, "172": 11, "178": 172, "50": 2, "55": 13, "60": 51, "66": 16, "163": 8, "85": 16, "86": 19, "87": 19, "88": 20, "89": 21, "90": 21, "91": 21, "92": 23, "93": 24, "94": 24, "95": 24, "96": 26, "97": 27, "98": 27, "99": 27, "100": 27, "101": 27, "102": 29, "103": 31, "104": 32, "105": 33, "106": 34, "107": 35, "108": 35, "109": 35, "110": 35, "111": 38, "112": 39, "113": 39, "114": 39, "115": 41, "116": 43, "117": 44, "118": 45, "119": 46, "120": 46, "121": 46, "122": 46, "123": 46, "124": 46, "125": 46, "126": 46, "127": 46}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
