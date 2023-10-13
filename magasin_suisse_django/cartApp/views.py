from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from cartApp.models import CartItem
from catalogApp.models import Product


def view_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart_items = CartItem.objects.filter(user=user)

        # Вычисляем общую сумму товаров в корзине
        total_price = sum(item.product.get_discounted_price() * item.quantity for item in cart_items)
    else:
        user = None
        cart_items = []
        total_price = 0  # Если пользователь не аутентифицирован, сумма равна 0.

    context = {
        'cart_items': cart_items,
        'user': user,
        'total_price': total_price,  # Добавляем общую сумму в контекст
    }

    return render(request, 'cartApp/cart.html', context)


def add_to_cart_by_slug(request, product_slug):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, product_slug=product_slug)
        user = request.user
        cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
    else:
        return JsonResponse({'error': 'Пользователь не аутентифицирован.'}, status=400)

    return JsonResponse({'success': True})


def remove_from_cart(request, product_id):
    if request.user.is_authenticated:
        user = request.user
        product = get_object_or_404(Product, product_id=product_id)
        cart_item = get_object_or_404(CartItem, user=user, product=product)
        cart_item.delete()
        return JsonResponse({'message': 'Товар удален из корзины.'})
    else:
        return JsonResponse({'error': 'Пользователь не аутентифицирован.'}, status=400)


def update_quantity(request, product_id, new_quantity):
    if request.method == 'PUT':  # Adjust the HTTP method
        cart_item = get_object_or_404(CartItem, product_id=product_id, user=request.user)
        cart_item.quantity = new_quantity
        cart_item.save()
        return JsonResponse({'message': 'Quantity updated successfully'})
    return JsonResponse({'error': 'Invalid request'})