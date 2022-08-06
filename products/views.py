from django.shortcuts import render
from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    template_name = 'products/product_list_view.html'
    model = Product
    context_object_name = 'products'
