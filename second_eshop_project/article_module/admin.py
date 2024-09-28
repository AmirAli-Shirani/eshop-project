from django.contrib import admin

from article_module.models import Article, ArticleCategory


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_active']
    list_editable = ['is_active']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # obj.author = request.user
        print(obj)

@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'is_active']
    list_editable = ['is_active', 'parent']
