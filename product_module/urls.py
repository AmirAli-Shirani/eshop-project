from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_lists'),
    path('cat/<cat>', views.ProductListView.as_view(), name='product_by_categories_lists'),
    path('brand/<brand>', views.ProductListView.as_view(), name='product_by_brands_lists'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product_detail')
]
