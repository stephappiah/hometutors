from django import template

register = template.Library()

# rounds floats to whole numbers
@register.filter
def dividebyth(value):
    value = round(value, 1)
    return value