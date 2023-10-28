# Generated by Django 4.2.4 on 2023-10-28 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('delivery_address', models.TextField()),
                ('delivery_postal_code', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('New', 'Новый'), ('Accepted', 'Принят'), ('Paid', 'Оплачен'), ('Completed', 'Выполнен'), ('In Progress', 'В процессе'), ('Preparing for Shipment', 'Готовится к отправке'), ('Being Delivered', 'Доставляется'), ('Delivered', 'Доставлен'), ('Canceled', 'Отменен')], default='Новый', max_length=225)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('item_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='payment_and_orders_App.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogApp.product')),
            ],
        ),
    ]
