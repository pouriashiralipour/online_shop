from django.shortcuts import render
from django.views import generic

from .models import Products


class ProductsListView(generic.ListView):
    template_name = 'products/products_list_view.html'
    model = Products
    context_object_name = 'products'
