from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext, gettext_lazy as _

from .models import Products, Comments
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


class CommentCreateView(SuccessMessageMixin, generic.CreateView):
    model = Comments
    form_class = CommentForm
    success_message = _('Your comment was successfully registered.')
    # def get_success_url(self):
    #     return reverse('products:details_view')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Products, id=product_id)
        obj.product = product

        return super().form_valid(form)
