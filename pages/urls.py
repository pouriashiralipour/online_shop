from django.urls import path

from .views import AboutUsView
from products.views import ProductsListView


app_name = 'pages'
urlpatterns = [
    path('', ProductsListView.as_view(), name='home_page'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
]
