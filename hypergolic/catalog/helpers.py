from django.utils.text import camel_case_to_spaces


def underscore(astring):
    return camel_case_to_spaces(astring).replace(' ', '_')
