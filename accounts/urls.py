from django.urls import path

from .views import password_change_success, login_after_password_change

app_name = 'generic'

urlpatterns = [
    path('password_change_success/', password_change_success, name="password_change_success"),
    path('password/change/', login_after_password_change,
         name='account_change_password'),
]
