from django import template

register = template.Library()


# takes in a price and a quantity as a parameters and returns their product
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
