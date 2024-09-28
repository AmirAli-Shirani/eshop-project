from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class ProductCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    url_title = models.CharField(max_length=200, verbose_name='عنوان در url', db_index=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی محصولات'


class ProductBrand(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام برند', db_index=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    url_title = models.CharField(max_length=200, verbose_name='عنوان در url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان محصول', db_index=True)
    category = models.ForeignKey(ProductCategory, verbose_name='دسته بندی محصول', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='آدرس تصویر')
    brand = models.ForeignKey(ProductBrand, verbose_name='برند', on_delete=models.CASCADE, null=True)
    price = models.IntegerField(verbose_name='قیمت محصول')
    short_description = models.CharField(max_length=200, verbose_name='توضیحات کوتاه محصول')
    description = models.TextField(verbose_name='توضیحات محصول')
    slug = models.SlugField(unique=True, verbose_name='عنوان در url', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='پاک شده نشده')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def __str__(self):
        return f'{self.title} / {self.price}'

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
