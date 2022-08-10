from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list_view'),
    path('<int:pk>/', views.ProductDetailsView.as_view(), name='product_details_view'),
    path('comments/<int:product_id>', views.CommentCreateView.as_view(), name='comment_create_view'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
