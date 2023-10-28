from django.contrib import admin
from .models import Requisites

class RequisitesAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'iban', 'bic_swift', 'bank_name', 'twint')
    search_fields = ('name', 'address', 'iban', 'bic_swift', 'bank_name', 'twint')

admin.site.register(Requisites, RequisitesAdmin)
