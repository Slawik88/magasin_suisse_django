from django.db import models


class Requisites(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    iban = models.CharField(max_length=30, verbose_name='IBAN')
    bic_swift = models.CharField(max_length=20, verbose_name='BIC/SWIFT')
    bank_name = models.CharField(max_length=255, verbose_name='Название банка')
    twint = models.CharField(max_length=20, verbose_name='TWINT')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Реквізити'
        verbose_name_plural = 'Реквізити'

