from django.shortcuts import render
from django.views import generic

from .models import Products
from .forms import CommentForm


class ProductsListView(generic.ListView):
    template_name = 'products/products_list_view.html'
    paginate_by = 8
    # model = Products
    queryset = Products.objects.filter(active=True)
    context_object_name = 'products'


class ProductDetailsView(generic.DetailView):
    model = Products
    template_name = 'products/product_details_view.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
