# Generated by Django 4.2.4 on 2023-10-26 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersApp', '0002_alter_customuser_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='postal_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]