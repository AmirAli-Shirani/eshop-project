# Generated by Django 4.2.7 on 2023-12-11 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'دسته بندی محصول', 'verbose_name_plural': 'دسته بندی محصولات'},
        ),
    ]
