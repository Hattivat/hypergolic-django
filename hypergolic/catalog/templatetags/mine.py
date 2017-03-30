from django import template

register = template.Library()


@register.filter
def spacify(astring):
    return astring.replace('_', ' ')