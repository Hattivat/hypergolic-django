from django import template
from django.forms.models import model_to_dict

register = template.Library()


@register.filter
def spacify(astring):
    return astring.replace('_', ' ')


@register.filter
def hashfind(obj, key):
    obj = model_to_dict(obj)
    if key in obj:
        return obj[key]
    else:
        return None
