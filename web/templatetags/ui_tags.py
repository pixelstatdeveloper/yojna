from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")


# Refer: https://stackoverflow.com/a/18951166/15733823
@register.filter
@stringfilter
def template_exists(value):
    try:
        template.loader.get_template(value)
        return True
    except template.TemplateDoesNotExist:
        return False
