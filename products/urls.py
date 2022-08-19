from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list_view'),
    path('<str:slug>/', views.product_details_view, name='product_details_view'),
    re_path(r'(?P<slug>[-\w]*)/$', views.product_details_view, name='product_details_view'),
    path('comments/<str:slug>', views.CommentCreateView.as_view(), name='comment_create_view'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    # path('category/<str:pk>', views.CategoryListView.as_view(), name='category_list_view'),
]
