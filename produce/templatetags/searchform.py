from django import template

from produce.forms import ProduceSearchForm

register = template.Library()

@register.simple_tag
def search_form(parser, token):
    return ProduceSearchForm()