from django import template

register = template.Library()


@register.filter(name='get_display')
def get_display(value, arg):
    return dict(arg).get(value, value)
