from django import template

register=template.Library()


@register.simple_tag(name='get_total') #decorator for modify function   the name is used to load in template page
def get_total(cart):
    total=0
    for item in cart.added_items.all():
        total+=item.quantity*item.product.price
    return total
  
