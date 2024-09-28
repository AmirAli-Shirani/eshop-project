from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from product_module.models import Product


# Create your views here.
class ProductListView(ListView):
    template_name = 'product_module/product-list.html'
    model = Product
    context_object_name = 'products'


class ProductDetailView(DetailView):
    template_name = 'product_module/product-detail.html'
    model = Product
    slug_field = 'slug'
    context_object_name = 'product'
