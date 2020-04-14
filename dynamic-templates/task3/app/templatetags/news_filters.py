from django import template
from datetime import datetime

register = template.Library()


@register.filter
def format_date(value):
    fmt = '%Y-%m-%d'
    now_date = datetime.now()
    posted_time = datetime.fromtimestamp(value)
    difference = now_date - posted_time
    difference_sec = difference.total_seconds()
    difference_min = difference_sec / 60
    difference_hour = difference_min / 60
    if difference_min <= 10:
        return "только что"
    elif difference_hour <= 24:
        difference_hour = round(difference_hour)
        ver1 = [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        ver2 = [1,21]
        ver3 = [2,3,4,22,23,24]
        if difference_hour in ver1:
            return f"{difference_hour} часов назад"
        elif difference_hour in ver2:
            return f"{difference_hour} час назад"
        elif difference_hour in ver3:
            return f"{difference_hour} часа назад"
    else:
        posted_time = datetime.strftime(posted_time, fmt)
        return posted_time



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
