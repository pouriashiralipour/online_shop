from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator

from .models import Product, Comments
from .forms import CommentsForm


class ProductListView(generic.ListView):
    template_name = 'products/product_list_view.html'
    # model = Product
    paginate_by = 8
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'


def product_details_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product_comments = product.comments.all()
    if request.method == "POST":
        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentsForm()
    else:
        comment_form = CommentsForm()
    return render(
        request,
        'products/product_details_view.html',
        {
            'product': product,
            'comment_form': comment_form,
            'product_comments': product_comments,


        }
    )


# class ProductDetailsView(generic.DetailView):
#     template_name = 'products/product_details_view.html'
#     model = Product
#     context_object_name = 'product'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comment_from'] = CommentsForm()
#         return context
#
#
class CommentCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Comments
    form_class = CommentsForm
    redirect_field_name = 'redirect_to'
    success_message = _("Your comment has been registered successfully and will be placed on the Sabbath after review")

    def form_valid(self, form):
        new_comment = form.save(commit=False)
        new_comment.author = self.request.user
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        new_comment.product = product
        return super().form_valid(form)


class SearchResultsView(generic.ListView):
    template_name = 'products/search_results.html'
    model = Product
    context_object_name = 'products_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(title__icontains=query)
