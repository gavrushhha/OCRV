import typing as tp
from datetime import timedelta
from django import template

T = tp.TypeVar('T')
register = template.Library()

@register.filter(name='change_timedelta')
def change_timedelta(value: int) -> str:
    return str(timedelta(seconds=value))


@register.filter(name='null_replace')
def null_replace(value: T) -> tp.Union[T, str]:
    if value == "NULL":
        return "-"
    return value