from  django import template

register = template.Library()

@register.simple_tag
def site_settings():
    pass
