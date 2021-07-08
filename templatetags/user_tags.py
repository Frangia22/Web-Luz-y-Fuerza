from django import template
from django.contrib.auth.models import Group
register = template.Library()
@register.filter
def absoluto(value):
    return abs(value)
@register.filter(name='grupo')
def grupo(usuario, grupo):
    return usuario.groups.filter(name=grupo).exists()