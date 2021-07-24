from django import template

register = template.Library()

@register.filter()
def remainder(n):
    return n % 3

@register.simple_tag
def numbers_to_bullets(number, total):
    black = u'\u2B24' * number
    white = u'\u25CB' * (total - number)
    return black + white