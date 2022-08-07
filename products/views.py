from django.shortcuts import render
from django.views import generic

from .models import Product, Comments
from .forms import CommentsForm


class ProductListView(generic.ListView):
    template_name = 'products/product_list_view.html'
    # model = Product
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'


class ProductDetailsView(generic.DeleteView):
    template_name = 'products/product_details_view.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_from'] = CommentsForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comments
    form = CommentsForm

    def form_valid(self, form):
        new_comment = form.save(commit=False)
        new_comment.author = self.request.user
        return super().form_valid(form)