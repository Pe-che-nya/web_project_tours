from django import template
register = template.Library()

#@register.simple_tag()
# def filter_departure(short_name, other_dic):
#     return other_dic[short_name]
@register.filter()
def filter_departure(text, dict):
    return dict[text]


@register.filter()
def get_stars(count):
    star="&#9733;"
    stars=""
    for i in range(int(count)):
        stars+=star
    return stars


# @register.filter()
# def get_departure(departure):




