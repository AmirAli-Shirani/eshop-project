# Generated by Django 4.2.7 on 2023-12-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0004_user_email_active_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, max_length=50, null=True, upload_to='', verbose_name='تصویر آواتار'),
        ),
    ]
