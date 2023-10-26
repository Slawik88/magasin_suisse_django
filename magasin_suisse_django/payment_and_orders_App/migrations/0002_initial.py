# Generated by Django 4.2.4 on 2023-10-26 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment_and_orders_App', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customerinfo',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payment_and_orders_App.order'),
        ),
    ]
