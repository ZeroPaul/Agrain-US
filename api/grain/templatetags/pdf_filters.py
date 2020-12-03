from django import template
from io import StringIO
import urllib, base64

register = template.Library()

@register.filter
def redecimal(number):
    number_float = float(number)
    number = str(round(number_float, 2))
    return number

@register.filter
def get_item(dictionary, key):
    return (dictionary.get(key),dictionary)
