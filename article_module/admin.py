from django.contrib import admin

from . import models


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'parent', 'is_active']
    list_editable = ['url_title', 'is_active', 'parent']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active']
    list_editable = ['is_active','slug']


admin.site.register(models.ArticleCategory, ArticleCategoryAdmin)
admin.site.register(models.Articles, ArticleAdmin)
