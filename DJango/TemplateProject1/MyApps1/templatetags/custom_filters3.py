from django import template

register = template.Library()


# @register.filter(name='truncate5')
def truncate5(value):
    result = value[0:5]
    return result


register.filter('truncate5', truncate5)
