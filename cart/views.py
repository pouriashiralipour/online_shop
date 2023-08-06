from django.shortcuts import render, get_object_or_404, redirect

from .cart import Cart
from .forms import AddToCartProductForm
from products.models import Products


def cart_page(request):
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, 'cart/cart.html')


def add_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Products, id=product_id)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity)

    return redirect('cart:cart_detail')

