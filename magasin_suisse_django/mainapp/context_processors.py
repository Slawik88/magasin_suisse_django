from django.contrib.auth import get_user

from cartApp.models import CartItem


def calculate_cart_total(user):
    total = 0
    if user.is_authenticated:
        cart_items = CartItem.objects.filter(user=user)
        for cart_item in cart_items:
            total += cart_item.quantity * cart_item.product.product_price
    return total


def cart_total(request):
    # Получите общую сумму товаров в корзине
    total = calculate_cart_total(request.user)
    return {'cart_total': total}


def get_username(request):
    user = get_user(request)
    username = user.username if user.is_authenticated else None
    return {'username': username}
