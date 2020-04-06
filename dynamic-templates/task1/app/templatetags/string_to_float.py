from django import template

register = template.Library()


@register.filter
def string_to_float(s):
    i = float(s)
    return i
