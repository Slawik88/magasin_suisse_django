# Generated by Django 4.2.4 on 2023-08-22 08:20

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='Назва')),
                ('category_description', models.TextField(max_length=100, null=True, verbose_name='Опис')),
                ('category_image', models.ImageField(upload_to='images/category_images/', verbose_name='Зображення')),
                ('category_slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='category_name', unique=True, verbose_name='Слаг(Автоматический)')),
                ('category_created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата створення')),
                ('category_updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalogApp.category', verbose_name='Вкладеність')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Swiper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='1400x400', upload_to='images/swiper_images/', verbose_name='Зображення на слайдер')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_article', models.IntegerField(db_index=True, help_text='Артикль МОЖЕ повторюватись.', verbose_name='Артикул')),
                ('product_name', models.CharField(max_length=50, verbose_name='Назва')),
                ('product_main_image', models.ImageField(help_text='Завантажте зображення для товару', upload_to='images/product_main_image/%Y/%m/%d/', verbose_name='Зображення до товару')),
                ('product_image_1', models.ImageField(blank=True, help_text='Додаткове зображення до товару', upload_to='images/product_main_image/%Y/%m/%d/', verbose_name='Зображення 1')),
                ('product_image_2', models.ImageField(blank=True, help_text='Додаткове зображення до товару', upload_to='images/product_main_image/%Y/%m/%d/', verbose_name='Зображення 2')),
                ('product_image_3', models.ImageField(blank=True, help_text='Додаткове зображення до товару', upload_to='images/product_main_image/%Y/%m/%d/', verbose_name='Зображення 3')),
                ('product_image_4', models.ImageField(blank=True, help_text='Додаткове зображення до товару', upload_to='images/product_main_image/%Y/%m/%d/', verbose_name='Зображення 4')),
                ('product_image_5', models.ImageField(blank=True, help_text='Додаткове зображення до товару', upload_to='images/product_main_image/%Y/%m/%d/', verbose_name='Зображення 5')),
                ('product_image_6', models.ImageField(blank=True, help_text='Додаткове зображення до товару', upload_to='images/product_main_image/%Y/%m/%d/', verbose_name='Зображення 6')),
                ('product_image_7', models.ImageField(blank=True, help_text='Додаткове зображення до товару', upload_to='images/product_main_image/%Y/%m/%d/', verbose_name='Зображення 7')),
                ('product_image_8', models.ImageField(blank=True, help_text='Додаткове зображення до товару', upload_to='images/product_main_image/%Y/%m/%d/', verbose_name='Зображення 8')),
                ('product_image_9', models.ImageField(blank=True, help_text='Додаткове зображення до товару', upload_to='images/product_main_image/%Y/%m/%d/', verbose_name='Зображення 9')),
                ('product_image_10', models.ImageField(blank=True, help_text='Додаткове зображення до товару', upload_to='images/product_main_image/%Y/%m/%d/', verbose_name='Зображення 10')),
                ('product_price', models.IntegerField(verbose_name='Ціна')),
                ('product_discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('product_slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='product_name', unique=True, verbose_name='Слаг(Автоматический)')),
                ('product_description', models.TextField(help_text='Максимум 2200 символів *', max_length=2200, verbose_name='Повний опис')),
                ('product_time_create', models.DateTimeField(auto_now_add=True, help_text='Відображає дату створення товару\nНіде не відображається тільки для адмінів*', verbose_name='Дата створення продукту')),
                ('product_time_update', models.DateTimeField(auto_now=True, help_text='Відображає дату оновлення товару\nНіде не відображається тільки для адмінів*', verbose_name='Дата оновлення продукту')),
                ('product_detalis', models.TextField(help_text='Вы можете указати колір або розмір ', max_length='999', verbose_name='Додаткова інформація')),
                ('product_category', models.ForeignKey(blank=True, help_text='Оберіть категорію в котрій буде продукт', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogApp.category', verbose_name='Категорія')),
            ],
        ),
    ]
