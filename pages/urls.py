from django.urls import path

from .views import HomePageView, ContactUsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('contact_us/', ContactUsView.as_view(), name='about_page'),
]
