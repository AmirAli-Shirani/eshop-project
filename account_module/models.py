from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(max_length=50, verbose_name='تصویر آواتار', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعال سازی ایمیل', null=True,blank=True)
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()
