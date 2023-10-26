from django.contrib import admin
from .forms import CustomerInfoForm
from .models import Order, OrderItem, CustomerInfo


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class CustomerInfoInline(admin.TabularInline):
    model = CustomerInfo
    can_delete = False
    form = CustomerInfoForm

    fieldsets = (
        ('Основная информация', {
            'classes': ('collapse',),
            'fields': ('order', 'first_name', 'last_name'),
        }),
        ('Адрес доставки', {
            'classes': ('collapse',),
            'fields': ('delivery_address', 'delivery_postal_code'),
        }),
        ('Контактная информация', {
            'classes': ('collapse',),
            'fields': ('email', 'notes'),
        }),
    )




class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline, CustomerInfoInline]

    list_display = ('id', 'status', 'customer', 'total_price',)
    list_filter = ('status', 'customer', 'created_at',)
    search_fields = ('customer__username', 'id',)


admin.site.register(Order, OrderAdmin)
