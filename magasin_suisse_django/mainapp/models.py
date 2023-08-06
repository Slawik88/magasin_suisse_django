from django.db import models
from mptt.fields import TreeForeignKey
from autoslug import AutoSlugField
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class Category(MPTTModel):
    category_name = models.CharField(max_length=50,
                            verbose_name='Назва')
    category_description = models.TextField(max_length=100, null=True,
                                   verbose_name='Опис')
    category_image = models.ImageField(upload_to='images/category_images/',
                              verbose_name='Зображення')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            db_index=True,
                            verbose_name='Вкладеність')
    category_slug = AutoSlugField(populate_from='category_name', unique=True, always_update=True,
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
# class Product(models.Model):


