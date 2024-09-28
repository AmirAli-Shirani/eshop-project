from django.db import models
from django.urls import reverse


# Create your models here.
class ContactUs(models.Model):
    fullName = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمبل')
    title = models.CharField(max_length=400, verbose_name='عنوان تماس با ما')
    message = models.TextField(verbose_name='متن تماس با ما')
    created_day = models.DateTimeField(verbose_name='تاریخ ایجاد شده', auto_now_add=True)
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین', null=True, blank=True)
    admin_response = models.TextField(null=True, blank=True, verbose_name='پاسخ توسط ادمین')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'مجموع تماس با ما'
