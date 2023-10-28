from django.contrib import admin

from .models import CartItem


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    list_filter = ('user', 'product')
    search_fields = ('user__username', 'product__product_name')
    list_per_page = 20


admin.site.register(CartItem, CartItemAdmin)
