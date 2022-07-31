from django import template
register = template.Library()


@register.filter()
def filter_departure(text, dict):
    return dict[text]


@register.filter()
def get_stars(count):
    star = "&#9733;"
    stars = ""
    for i in range(int(count)):
        stars += star
    return stars


@register.filter
def ru_plural(value, variants):
    variants = variants.split(",")
    value = abs(int(value))

    if value % 10 == 1 and value % 100 != 11:
        variant = 0
    elif value % 10 >= 2 and value % 10 <= 4 and \
            (value % 100 < 10 or value % 100 >= 20):
        variant = 1
    else:
        variant = 2

    return variants[variant]


@register.filter()
def max_smth(dic, cat):

    lst = []
    for k in dic:
        lst.append(dic[k][cat])
    maximum = max(lst)
    return maximum


@register.filter()
def min_smth(dic, cat):

    lst = []
    for k in dic:
        lst.append(dic[k][cat])
    minimum = min(lst)
    return minimum


@register.filter()
def func(dic, dep):

    val = dic[dep]
    return val
