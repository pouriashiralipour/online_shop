from django.shortcuts import render

from .forms import OrderForm


def order_create_view(request):
    context = {'form': OrderForm()}
    return render(request, 'orders/order_create.html', context)
