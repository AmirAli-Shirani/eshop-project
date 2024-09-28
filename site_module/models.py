from django.db import models


# Create your models here.
class SiteSettings(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان سایت', null=True, blank=True)
    text = models.TextField(verbose_name='متن درباره ما')
    image = models.ImageField(upload_to='images/about-us', verbose_name='لوگو سایت')
    email = models.EmailField(verbose_name='ایمیل')
    number = models.CharField(max_length=200, verbose_name='تلفن تماس')
    address = models.CharField(max_length=500, verbose_name='آدرس')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.title


class SiteBanner(models.Model):
    class SiteBannerChoices(models.TextChoices):
        product_list = 'product_list', 'صفحه ی لیست محصولات'
        product_detail = 'product_detail', 'صفحه ی جزییات محصول'
        about_us = 'about_us', 'صفحه ی درباره ما'
        article_page = 'article_page', 'صفحه ی مقالات '

    title = models.CharField(max_length=200, verbose_name='عنوان بنر')
    url = models.URLField(verbose_name='آدرس بنر')
    image = models.ImageField(upload_to='images/banners', verbose_name='تصویر بنر')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')
    position = models.CharField(max_length=200, choices=SiteBannerChoices.choices, verbose_name='محل استفاده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بنر تبلیغاتی'
        verbose_name_plural = 'بنر های تبلیغاتی'


class SiteSlider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    sub_title = models.CharField(max_length=200, verbose_name='عنوان کوچک')
    short_description = models.TextField(verbose_name='توضیحات کوتاه اسلایدر')
    image = models.ImageField(upload_to='images/sliders', verbose_name='عکس اسلایدر')
    is_active=models.BooleanField(default=True,verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اسلایدر صفحه اصلی'
        verbose_name_plural = 'اسلایدر های صفحه اصلی'
