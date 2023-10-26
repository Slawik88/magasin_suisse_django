from django.db import transaction
from django.http import JsonResponse
from .models import Order, OrderItem
from .forms import OrderForm
from .models import CustomUser
from cartApp.models import CartItem
from catalogApp.models import Category
from django.shortcuts import render, redirect


def create_order_instance(user, form, cart_items, total_price):
    """
    Создает экземпляр заказа и сохраняет его вместе с пунктами заказа.
    """
    with transaction.atomic():
        order = Order(
            customer=user,
            total_price=total_price,
            # Устанавливайте остальные поля формы
        )
        order.save()

        for cart_item in cart_items:
            order_item = OrderItem(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                item_price=cart_item.product.product_price
            )
            order_item.save()

        cart_items.delete()


def get_cart_info(user):
    """
    Получает информацию о корзине и общей стоимости.
    """
    cart_items = CartItem.objects.filter(user=user)
    total_price = 0

    for cart_item in cart_items:
        cart_item.total_price = cart_item.quantity * cart_item.product.product_price
        total_price += cart_item.total_price

    return cart_items, total_price


def order_and_payment(request):
    # Query the data you need from your models
    categories = Category.objects.all()

    cart_items, total_price = get_cart_info(request.user)

    try:
        user_data = CustomUser.objects.get(pk=request.user.pk)
    except CustomUser.DoesNotExist:
        user_data = None

    form = OrderForm(initial={
        'first_name': user_data.first_name if user_data else '',
        'last_name': user_data.last_name if user_data else '',
        'delivery_address': user_data.shipping_address if user_data else '',
        'email': user_data.email if user_data else '',
        'phone_number': user_data.phone_number if user_data else '',
        'delivery_postal_code': user_data.postal_code if user_data else '',
    })

    context = {
        'form': form,
        'categories': categories,
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, 'payment_and_orders_App/payment_form.html', context)


def save_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cart_items, total_price = get_cart_info(request.user)

            try:
                create_order_instance(request.user, form, cart_items, total_price)

                return redirect('profile')

            except Exception as e:
                return JsonResponse({'success': False, 'message': f'Error: {str(e)}'})
    return JsonResponse({'success': False, 'message': 'Invalid form data.'})
