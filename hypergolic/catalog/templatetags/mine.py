from django import template
from django.forms.models import model_to_dict
from django.core.exceptions import FieldDoesNotExist

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
    try:
        return obj._meta.get_field(field).verbose_name
    except FieldDoesNotExist:
        return field.replace('_', ' ')


@register.filter
def classy(obj):
    return obj.__class__.__name__


@register.filter
def dot(obj, lookup):
    if hasattr(obj, lookup):
        try:
            return getattr(obj, lookup)()
        except TypeError:
            return getattr(obj, lookup)
    else:
        return '-'
