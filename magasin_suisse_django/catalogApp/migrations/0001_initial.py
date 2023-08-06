# Generated by Django 4.2.4 on 2023-08-06 10:27

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
    ]
