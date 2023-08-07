from django.urls import path

from .views import cart_page, add_to_cart_view

app_name = 'cart'
urlpatterns = [
    path('', cart_page, name='cart_detail'),
    path('add/<int:product_id>/', add_to_cart_view, name='add'),
]
