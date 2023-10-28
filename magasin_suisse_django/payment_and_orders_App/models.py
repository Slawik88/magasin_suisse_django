from django.db import models

from catalogApp.models import Product
from usersApp.models import CustomUser


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('New', 'Новий'),
        ('Accepted', 'Прийнятий'),
        ('Paid', 'Сплачений'),
        ('Completed', 'Виконаний'),
        ('In Progress', 'В процесі'),
        ('Preparing for Shipment', 'Готується до відправлення'),
        ('Being Delivered', 'Доставляється'),
        ('Delivered', 'Доставлений'),
        ('Canceled', 'Скасований'),
    ]

    status = models.CharField(max_length=225, choices=ORDER_STATUS_CHOICES, default='Новий', verbose_name='Статус')

    customer = models.ForeignKey(CustomUser,
                                 on_delete=models.CASCADE,
                                 verbose_name='Користувач')  # Припускається, що ви використовуєте вбудовану модель користувача
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Загальна вартість')

    def __str__(self):
        return f'Замовлення №{self.pk} від {self.customer.username}'

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Замовлення')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Кількість')
    item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Ціна товару')

    def save(self, *args, **kwargs):
        self.item_price = self.product.product_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.quantity} x {self.product.product_name}'

    class Meta:
        verbose_name = 'Позиція замовлення'
        verbose_name_plural = 'Позиції замовлення'


class CustomerInfo(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name='Замовлення')
    first_name = models.CharField(max_length=100, verbose_name="Ім'я")
    last_name = models.CharField(max_length=100, verbose_name='Прізвище')
    delivery_address = models.TextField(verbose_name='Адреса доставки')
    delivery_postal_code = models.CharField(max_length=10, verbose_name='Поштовий індекс')
    email = models.EmailField(verbose_name='Електронна пошта')
    notes = models.TextField(blank=True, verbose_name='Примітки')  # Зробити примітки необов'язковими

    def __str__(self):
        return f'Інформація про клієнта для замовлення №{self.order.pk}'

    class Meta:
        verbose_name = 'Інформація про клієнта'
        verbose_name_plural = 'Інформація про клієнтів'
