from django.contrib import admin
from .models import Product, ProductCategory, ProductBrand


# Register your models here.
@admin.register(Product)
class Admin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'is_active', 'is_delete']
    list_editable = ['is_active', 'is_delete', 'category']


@admin.register(ProductCategory)
class Admin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'is_active']
    list_editable = ['is_active']


@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active']
