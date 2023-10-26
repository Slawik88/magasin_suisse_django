from django.db import models

from catalogApp.models import Product
from usersApp.models import CustomUser


class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('New', 'Новый'),
        ('Accepted', 'Принят'),
        ('Paid', 'Оплачен'),
        ('Completed', 'Выполнен'),
        ('In Progress', 'В процессе'),
        ('Preparing for Shipment', 'Готовится к отправке'),
        ('Being Delivered', 'Доставляется'),
        ('Delivered', 'Доставлен'),
        ('Canceled', 'Отменен'),
    ]

    status = models.CharField(max_length=225, choices=ORDER_STATUS_CHOICES, default='Новый')

    customer = models.ForeignKey(CustomUser,
                                 on_delete=models.CASCADE)  # Предполагается, что вы используете встроенную модель пользователя
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Order #{self.pk} by {self.customer.username}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Замените Product на свою модель товаров
    quantity = models.PositiveIntegerField(default=1)
    item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.item_price = self.product.product_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.quantity} x {self.product.product_name}'


class CustomerInfo(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    delivery_address = models.TextField()
    delivery_postal_code = models.CharField(max_length=10)
    email = models.EmailField()
    notes = models.TextField(blank=True)  # Make notes optional

    def __str__(self):
        return f'Customer Info for Order #{self.order.pk}'
