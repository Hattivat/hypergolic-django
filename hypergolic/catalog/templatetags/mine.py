from django import template
from django.forms.models import model_to_dict

register = template.Library()


@register.filter
def spacify(astring):
    return astring.replace('_', ' ')


@register.filter
def to_dict(obj):
    return model_to_dict(obj)


@register.filter
def hashfind(dic, key):
    if key in dic:
        return dic[key]
    else:
        return '-'


@register.filter
def attr(obj, arg1):
    att, value = arg1.split(":")
    obj.field.widget.attrs[att] = value
    return obj


@register.filter
def verbose_name(obj, field):
    return obj._meta.get_field(field).verbose_name
