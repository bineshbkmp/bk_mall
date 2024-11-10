from django import template

register=template.Library()


@register.simple_tag(name='multiply') #decorator for modify function   the file-name is used in load statement,  in template page
def multiply(a,b):
    return a*b
  
