from django.utils.text import camel_case_to_spaces


def underscore(astring):
    return camel_case_to_spaces(astring).replace(' ', '_')


def wrong_year_order(y1, y2):
    if y1 and y2:
        if int(y1) > int(y2):
            return True
    return False


def strip_mid_whitespace(astring):
    return " ".join(astring.split())
