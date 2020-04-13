from django import template
from datetime import datetime

register = template.Library()


@register.filter
def format_date(value):
    a = datetime.strptime(str(value), '%m/%d/%y %H:%M:%S')
    return a


@register.filter
def score(value):
    if value <= - 5:
        return f"{value} (все плохо)"
    elif -5 < value < 5:
        return f"{value} (нейтрально)"
    elif value > 5:
        return f"{value} (хорошо)"


@register.filter
def format_num_comments(value):
    if value == 0:
        return "Оставьте комментарий"
    elif 0 < value <= 50:
        return value
    elif value > 50:
        return "50+"


@register.filter
def format_selftext(cstr, count):
    nstr = cstr.split()
    if len(nstr) <= count * 2:
        return cstr
    string = ""
    for i in range(count):
        string += nstr[i] + " "
    string += " ... "
    for i in range(count):
        string += nstr[i - count] + " "
    return string
