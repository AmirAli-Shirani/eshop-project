from django.db import models
from django.urls import reverse

from account_module.models import User


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی محصولات'

    def __str__(self):
        return self.title


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام برند', null=True, db_index=True)
    url_title = models.CharField(max_length=200, verbose_name='نام در url', db_index=True)
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال', default=True)

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='دسته بندی ها')
    image = models.ImageField(upload_to='images/products', verbose_name='عکس محصول', null=True, blank=True)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='برند', null=True)
    price = models.CharField(max_length=200, verbose_name='قیمت')
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(max_length=500, verbose_name='توضیحات اصلی', db_index=True)
    slug = models.SlugField(default='', null=False, db_index=True, blank=True)
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} / ({self.price})'

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductsTags(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'تگ محصولات'
        verbose_name_plural = 'تگ های محصولات'


class ProductVisit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')

    def __str__(self):
        return f'{self.product.title} / {self.ip}'

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدید های محصول'


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='برای محصول')
    image = models.ImageField(upload_to='images/product_gallery', verbose_name='تصویر گالری')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'تصویر گالری'
        verbose_name_plural = 'تصاویر گالری'
