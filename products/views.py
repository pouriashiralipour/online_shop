from django.shortcuts import render
from django.views import generic

from .models import Products


class ProductsListView(generic.ListView):
    template_name = 'products/products_list_view.html'
    model = Products
    context_object_name = 'products'


class ProductDetailsView(generic.DetailView):
    model = Products
    template_name = 'products/product_details_view.html'
