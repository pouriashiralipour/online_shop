from django.shortcuts import render
from django.views import generic

from .models import Product


class ProductListView(generic.ListView):
    template_name = 'products/product_list_view.html'
    # model = Product
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'


class ProductDetailsView(generic.DeleteView):
    template_name = 'products/product_details_view.html'
    model = Product
    context_object_name = 'product'
