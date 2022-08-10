from django.shortcuts import render
from django.views import generic

from products import models


class HomePageView(generic.ListView):
    template_name = 'products/product_list_view.html'
    # model = Product
    queryset = models.Product.objects.filter(active=True)
    context_object_name = 'products'


class ContactUsView(generic.TemplateView):
    template_name = 'pages/contact_us.html'
