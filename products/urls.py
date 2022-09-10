from django.urls import path, re_path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list_view'),
    # path('<str:slug>/', views.product_details_view, name='product_details_view'),
    re_path(r'(?P<slug>[-\w]*)/$', views.ProductDetailsView.as_view(), name='product_details_view'),
    path('comments/<str:slug>', views.CommentCreateView.as_view(), name='comment_create_view'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    # path('search/page/<int:page>', views.SearchResultsView.as_view(), name='search_results'),
    re_path(r'category/(?P<slug>[-\w]*)/$', views.CategoryListView.as_view(), name='category-list_view'),
]
