from django.urls import path

from . import views
from .views import view_cart

urlpatterns = [
    path('', view_cart, name='cart'),
    path('add_to_cart_by_slug/<slug:product_slug>/', views.add_to_cart_by_slug, name='add_to_cart_by_slug'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update_quantity/<int:product_id>/<int:new_quantity>/', views.update_quantity, name='update_quantity'),
]
