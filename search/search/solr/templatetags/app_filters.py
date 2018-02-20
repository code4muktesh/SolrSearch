from django import template
from django.utils.safestring import mark_safe
register = template.Library()
 
@register.filter(name='lookup')
def lookup(d, key):
    return d[key]
@register.filter(name='getContentFromJsonSolrResult')
def getContentFromHiglights(d, key):
    data=d[key]
    return  mark_safe(d[key]["content"][0])

