from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from order_module.models import Order
from site_module.models import SiteBanner
from utils.convertors import group_list
from .models import Product, ProductCategory, ProductBrand, ProductGallery


class ProductListView(ListView):
    template_name = 'product_module/product-lists.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['banners'] = SiteBanner.objects.filter(is_active=True,
                                                       position__iexact=SiteBanner.SiteBannerChoices.product_list)
        return context

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        if brand_name is not None:
            query = query.filter(brand__url_title__iexact=brand_name)

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query


class ProductDetailView(DetailView):
    template_name = 'product_module/product-detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        loaded_products = self.object
        request = self.request
        latest_products = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')[:8]
        context['latest_products'] = group_list(latest_products)
        context['related_products'] = group_list(
            list(Product.objects.filter(brand_id=loaded_products.brand_id).all()[:12]), 3)
        context['product_galleries_group'] = group_list(
            list(ProductGallery.objects.filter(product_id=loaded_products.id).all()), 3)
        if request.user.is_authenticated:
            order_cart=Order.objects.filter()
        # user_ip = get_client_ip(self.request)
        # user_id = None
        # if self.request.user.is_authenticated:
        #     user_id = self.request.user.id
        # has_been_visited = ProductVisit.objects.filter(ip__iexact=user_ip).exists()
        # if not has_been_visited:
        #     new_user=ProductVisit(ip=user_id,user_id=user_id,product_id=loaded_products.id)
        #     new_user.save()
        return context


def product_categories_components(request):
    product_category = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'categories': product_category
    }
    return render(request, 'product_module/components/product-categories.html', context)


def product_brands_components(request):
    product_brand = ProductBrand.objects.annotate(products_count=Count('product')).filter(is_active=True)
    context = {
        'brands': product_brand
    }
    return render(request, 'product_module/components/product-brands.html', context)
