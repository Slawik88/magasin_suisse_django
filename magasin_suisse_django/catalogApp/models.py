# Create your models here.
from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.

class Category(MPTTModel):
    category_name = models.CharField(max_length=50,
                                     verbose_name='Назва')
    category_description = models.TextField(max_length=100, null=True,
                                            verbose_name='Опис')
    category_image = models.ImageField(upload_to='images/category_images/',
                                       verbose_name='Зображення')
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True,
                            related_name='children',
                            db_index=True,
                            verbose_name='Вкладеність')
    category_slug = AutoSlugField(populate_from='category_name',
                                  unique=True,
                                  always_update=True,
                                  db_index=True,
                                  verbose_name='Слаг(Автоматический)')
    category_created_at = models.DateTimeField(auto_now_add=True,
                                               verbose_name='дата створення')
    category_updated_at = models.DateTimeField(auto_now=True,
                                               verbose_name='Дата оновлення')

    def save(self, *args, **kwargs):
        # Обновляем слаг перед сохранением объекта
        self.slug = self._meta.get_field('category_slug').slugify(self.category_name)
        super().save(*args, **kwargs)

    class MPTTMeta:
        order_insertion_by = ['category_name']

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        breadcrumbs = self.get_ancestors(include_self=True)
        url_parts = [breadcrumb.category_name for breadcrumb in breadcrumbs]
        return reverse('get_categoris_and_subcategories', kwargs={'category_slug': self.category_slug})


class Product(models.Model):

    product_id = models.AutoField(primary_key=True, unique=True, verbose_name='ID товара')
    product_article = models.IntegerField(db_index=True, verbose_name='Артикул',
                                          help_text='Артикль МОЖЕ повторюватись.')

    product_name = models.CharField(max_length=50,
                                    verbose_name='Назва')
    product_main_image = models.ImageField(upload_to='images/product_main_image/%Y/%m/%d/',
                                           verbose_name="Зображення до товару",
                                           help_text="Завантажте зображення для товару")
    product_image_1 = models.ImageField(upload_to='images/product_main_image/%Y/%m/%d/',
                                        verbose_name="Зображення 1",
                                        help_text="Додаткове зображення до товару", blank=True)
    product_image_2 = models.ImageField(upload_to='images/product_main_image/%Y/%m/%d/',
                                        verbose_name="Зображення 2",
                                        help_text="Додаткове зображення до товару", blank=True)
    product_image_3 = models.ImageField(upload_to='images/product_main_image/%Y/%m/%d/',
                                        verbose_name="Зображення 3",
                                        help_text="Додаткове зображення до товару", blank=True)
    product_image_4 = models.ImageField(upload_to='images/product_main_image/%Y/%m/%d/',
                                        verbose_name="Зображення 4",
                                        help_text="Додаткове зображення до товару", blank=True)
    product_image_5 = models.ImageField(upload_to='images/product_main_image/%Y/%m/%d/',
                                        verbose_name="Зображення 5",
                                        help_text="Додаткове зображення до товару", blank=True)
    product_image_6 = models.ImageField(upload_to='images/product_main_image/%Y/%m/%d/',
                                        verbose_name="Зображення 6",
                                        help_text="Додаткове зображення до товару", blank=True)
    product_image_7 = models.ImageField(upload_to='images/product_main_image/%Y/%m/%d/',
                                        verbose_name="Зображення 7",
                                        help_text="Додаткове зображення до товару", blank=True)
    product_image_8 = models.ImageField(upload_to='images/product_main_image/%Y/%m/%d/',
                                        verbose_name="Зображення 8",
                                        help_text="Додаткове зображення до товару", blank=True)
    product_image_9 = models.ImageField(upload_to='images/product_main_image/%Y/%m/%d/',
                                        verbose_name="Зображення 9",
                                        help_text="Додаткове зображення до товару", blank=True)
    product_image_10 = models.ImageField(upload_to='images/product_main_image/%Y/%m/%d/',
                                         verbose_name="Зображення 10",
                                         help_text="Додаткове зображення до товару", blank=True)

    product_price = models.IntegerField(verbose_name='Ціна')
    product_discount_price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)

    product_slug = AutoSlugField(populate_from='product_name',
                                 unique=True,
                                 always_update=True,
                                 db_index=True,
                                 verbose_name='Слаг(Автоматический)')
    product_description = models.TextField(max_length=2200, verbose_name='Повний опис',
                                           help_text="Максимум 2200 символів *")

    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name='Категорія', help_text='Оберіть категорію в котрій буде продукт')
    product_time_create = models.DateTimeField(auto_now_add=True,
                                               help_text="Відображає дату створення товару\nНіде не відображається тільки для адмінів*",
                                               verbose_name="Дата створення продукту")
    product_time_update = models.DateTimeField(auto_now=True,
                                               help_text="Відображає дату оновлення товару\nНіде не відображається тільки для адмінів*",
                                               verbose_name="Дата оновлення продукту", )

    product_details = models.TextField(max_length="999", verbose_name="Додаткова інформація", help_text="Вы можете указати колір або розмір ")




    def __str__(self):
        return f'{self.product_article} - {self.product_name}'

    def get_absolute_url(self):
        breadcrumbs = self.get_ancestors(include_self=True)
        url_parts = [breadcrumb.category_name for breadcrumb in breadcrumbs]
        return reverse('product_detail', kwargs={'product_slug': self.product_slug})

    class MPTTMeta:
        order_insertion_by = ['product_name']

    def get_discounted_price(self):
        if self.product_discount_price is not None:
            return self.product_discount_price
        else:
            return self.product_price


class Swiper(models.Model):
    image = models.ImageField(upload_to='images/swiper_images/', verbose_name='Зображення на слайдер',
                              help_text='1400x400')
