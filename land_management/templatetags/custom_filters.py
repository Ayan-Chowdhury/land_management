# your_app/templatetags/custom_filters.py
import os
from django import template

register = template.Library()

@register.filter
def basename(value):
    """Return the basename of a file path."""
    return os.path.basename(value)

@register.filter
def split(value, delimiter=' '):
    """Split the string by the given delimiter."""
    if isinstance(value, str):
        return value.split(delimiter)
    return value