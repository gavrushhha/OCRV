from datetime import timedelta
from django import template

register = template.Library()

@register.filter(name='change_timedelta')
def change_timedelta(value: int) -> str:
    return str(timedelta(seconds=value))