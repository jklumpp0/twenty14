def multiply(lhs, rhs, *args, **kwargs):
    return lhs * rhs

from django import template
register = template.Library()
register.simple_tag(multiply, name="multiply")

