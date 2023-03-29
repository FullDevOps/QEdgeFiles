# custom-filter with args(i/p-para)
from django import template

register = template.Library()


@register.filter(name='c_and_c')
def cut_and_concate(value, arg):
    result = value[:3] + str(arg)
    return result
# register.filter('c_and_c', cut_and_concate)
