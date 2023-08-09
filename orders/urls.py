from django.urls import path

from .views import order_create_view

app_name = 'order'
urlpatterns = [
    path('create/', order_create_view, name='create'),
]
