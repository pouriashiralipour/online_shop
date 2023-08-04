from django.urls import path

from .views import AboutUsView


app_name = 'pages'
urlpatterns = [
    path('about_us/', AboutUsView.as_view(), name='about_us'),
]
