from django.contrib import admin

from . import models

admin.site.register(models.Product)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductsTags)
admin.site.register(models.ProductBrand)
admin.site.register(models.ProductVisit)
admin.site.register(models.ProductGallery)
