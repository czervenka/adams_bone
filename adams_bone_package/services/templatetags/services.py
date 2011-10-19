import re
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django import template

register = template.Library()

@register.filter
def startswith(object, param):
    return object.startswith(param)

@register.inclusion_tag('inclusiontags/menu_item.html', takes_context=True)
def menu_item(context, item_path, title, url=None, with_subcategories=True):
    category = context.get('category', '')

    if url is None:
        url = '%s' % item_path

    if category:
        current_path = category.tree_path
    else:
        current_path = ''

    if with_subcategories:
        selected = current_path.startswith(item_path[1:])
    else:
        selected = current_path = item_path

    return {
        'selected': selected,
        'title': title,
        'url': url,
    }


@register.filter()
def obfuscate(email, linktext=None, autoescape=None):
    """
    Given a string representing an email address,
	returns a mailto link with rot13 JavaScript obfuscation.

    Accepts an optional argument to use as the link text;
	otherwise uses the email address itself.
    """
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x

    email = re.sub('@','\\\\100', re.sub('\.', '\\\\056', \
        esc(email))).encode('rot13')

    if linktext:
        linktext = esc(linktext).encode('rot13')
    else:
        linktext = email

    rotten_link = """<script type="text/javascript">document.write \
        ("<n uers=\\\"znvygb:%s\\\">%s<\\057n>".replace(/[a-zA-Z]/g, \
        function(c){return String.fromCharCode((c<="Z"?90:122)>=\
        (c=c.charCodeAt(0)+13)?c:c-26);}));</script>""" % (email, linktext)
    return mark_safe(rotten_link)
obfuscate.needs_autoescape = True
