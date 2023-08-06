from django.urls import path, re_path

from .views import ProductsListView, ProductDetailsView, CommentCreateView

app_name = 'products'
urlpatterns = [
    path('products/', ProductsListView.as_view(), name='list_view'),
    re_path(r'(?P<slug>[-\w]*)/$', ProductDetailsView.as_view(), name='details_view'),
    path('comment/<int:product_id>/', CommentCreateView.as_view(), name='comment_create_view'),
]
