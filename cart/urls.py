from django.urls import path

from .views import cart_page, add_to_cart_view, remove_from_cart, clear_cart

app_name = 'cart'
urlpatterns = [
    path('', cart_page, name='cart_detail'),
    path('add/<int:product_id>/', add_to_cart_view, name='add'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove'),
    path('clear/', clear_cart, name='clear'),
]
