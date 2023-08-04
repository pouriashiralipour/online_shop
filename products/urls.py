from django.urls import path, re_path

from .views import ProductsListView, ProductDetailsView

app_name = 'products'
urlpatterns = [
    path('', ProductsListView.as_view(), name='list_view'),
    re_path(r'(?P<slug>[-\w]*)/$', ProductDetailsView.as_view(), name='details_view'),
]
