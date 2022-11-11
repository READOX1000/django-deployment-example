from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cust out allvalue of "arg" from the string

    """
    return value.replace(arg, '')

# register.filter('cut', cut)
