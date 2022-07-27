import random
from django import template

register = template.Library()

@register.simple_tag
def random_choose(list):
    sample = random.choices(list, k=5)
    return sample
