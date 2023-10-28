from django.contrib import admin

from .models import Category, Swiper, Product


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Основні дані', {
            'fields': ['product_article', 'product_name', 'product_category', 'product_description', 'product_details']
        }),
        ('Головне зображення', {
            'fields': ['product_main_image']
        }),
        ('Додаткові зображення', {
            'fields': ['product_image_1', 'product_image_2', 'product_image_3', 'product_image_4', 'product_image_5',
                       'product_image_6', 'product_image_7', 'product_image_8', 'product_image_9', 'product_image_10'],
            'classes': ['collapse']
        }),
        ('Ціни', {
            'fields': ['product_price', 'product_discount_price']
        }),

    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Swiper)
