from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import gettext as _

from .cart import Cart
from .forms import AddToCartProductForm
from products.models import Products


def cart_page(request):
    cart = Cart(request)
    for item in cart:
        item['product_update_quantity_form'] = AddToCartProductForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })
    context = {'cart': cart}
    return render(request, 'cart/cart.html', context)


@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Products, id=product_id)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity, replace_current_quantity=cleaned_data['inplace'])

    return redirect('cart:cart_detail')


def remove_from_cart(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Products, id=product_id)

    cart.remove(product)

    return redirect('cart:cart_detail')


def clear_cart(request):
    cart = Cart(request)

    if len(cart):
        cart.clear()
        messages.success(request, _('Your cart was clear successfully.'))
    else:
        messages.warning(request, _('Your cart is already empty.'))
