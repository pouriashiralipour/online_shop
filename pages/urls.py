from django.urls import path

from .views import HomePageView, AboutUsView


app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
]
