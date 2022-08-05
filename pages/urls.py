from django.urls import path

from .views import HomePageView, AboutUsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('aboutus/', AboutUsView.as_view(), name='about_page'),
]
