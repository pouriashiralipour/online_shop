from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from .middleware import GetIPAddressMiddleWare

from .models import Product, Comments, Category
from .forms import CommentsForm


class ProductListView(generic.ListView):
    template_name = 'products/product_list_view.html'
    # model = Product
    paginate_by = 8
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'


# def product_details_view(request, slug=None):
#     product_obj = None
#     if slug is not None:
#         product_obj = get_object_or_404(Product, slug=slug)
#     context = {'comment_from': CommentsForm(), 'product': product_obj}
#     return render(
#         request,
#         'products/product_details_view.html',
#         context,
#     )


class ProductDetailsView(generic.DetailView):
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)
        ip_address = self.request.user.ip_address
        if ip_address not in product.hits.all():
            product.hits.add(ip_address)

        return product

    template_name = 'products/product_details_view.html'
    # model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_from'] = CommentsForm()
        return context


class CommentCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Comments
    form_class = CommentsForm
    redirect_field_name = 'redirect_to'
    success_message = _("Your comment has been registered successfully and will be placed on the Sabbath after review")

    def form_valid(self, form):
        new_comment = form.save(commit=False)
        new_comment.author = self.request.user
        slug = str(self.kwargs['slug'])
        product = get_object_or_404(Product, slug=slug)
        new_comment.product = product
        return super().form_valid(form)


class SearchResultsView(generic.ListView):
    template_name = 'products/search_results.html'
    model = Product
    context_object_name = 'products_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(title__icontains=query)


# def category_list_view(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     context = {
#         'category': category,
#     }
#     return render(request, 'products/category_list_view.html', context)

class CategoryListView(generic.ListView):
    paginate_by = 2
    template_name = 'products/category_list_view.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.filter(status=True), slug=slug)
        return category.products.filter(active=True)

    context_object_name = 'category'
