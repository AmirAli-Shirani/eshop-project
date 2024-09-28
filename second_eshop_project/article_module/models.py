from django.db import models

from account_module.models import User


# Create your models here.

class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', models.CASCADE, null=True, blank=True, verbose_name='دسته بندی والد')
    title = models.CharField(max_length=300, verbose_name='عنوان دسته بندی')
    url_title = models.CharField(max_length=400, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی های مقالات'


class Article(models.Model):
    title = models.CharField(max_length=400, verbose_name='عنوان مقاله')
    slug = models.SlugField(allow_unicode=True, verbose_name='عنوان در url')
    short_description = models.TextField(verbose_name='توضیحات کوتاه مقاله')
    description = models.TextField(verbose_name='توضحات اصلی')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر مقاله')
    categories = models.ManyToManyField(ArticleCategory, related_name='articles', verbose_name='دسته بندی ها')
    author = models.ForeignKey(User, verbose_name='نویسنده', on_delete=models.CASCADE , null=True , blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
