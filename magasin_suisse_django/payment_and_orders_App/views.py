from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from cartApp.models import CartItem
from catalogApp.models import Category
from .forms import OrderForm
from .models import CustomUser, Order, OrderItem, CustomerInfo


def create_order_instance(user, form, cart_items, total_price, first_name=None, last_name=None):
    """
    Создает экземпляр заказа и сохраняет его вместе с пунктами заказа.
    """
    with transaction.atomic():  # Используем транзакции для атомарности операций
        order = Order(
            customer=user,  # Устанавливаем пользователя, сделавшего заказ
            total_price=total_price,
            # Дополнительные поля формы могут быть установлены здесь
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

        if first_name is not None and last_name is not None:
            customer_info = CustomerInfo(
                order=order,
                first_name=first_name,
                last_name=last_name,
            )
            customer_info.save()

        cart_items.delete()  # Удаляем товары из корзины после создания заказа


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
    # Запрашиваем данные из моделей, которые потребуются для формы заказа
    categories = Category.objects.all()

    # Получаем данные о пользователе. Если пользователя не существует, получим 404 ошибку
    user_data = get_object_or_404(CustomUser, pk=request.user.pk)

    # Создаем экземпляр формы заказа и предзаполняем данными пользователя
    form = OrderForm(initial={
        'first_name': user_data.first_name,
        'last_name': user_data.last_name,
        'delivery_address': user_data.shipping_address,
        'email': user_data.email,
        'phone_number': user_data.phone_number,
        'delivery_postal_code': user_data.postal_code,
    })

    # Получаем информацию о корзине и общей стоимости
    cart_items, total_price = get_cart_info(request.user)

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
            # Получаем информацию о корзине и общей стоимости товаров
            cart_items, total_price = get_cart_info(request.user)
            first_name = request.user.first_name
            last_name = request.user.last_name

            try:
                create_order_instance(request.user, form, cart_items, total_price, first_name, last_name)
                return redirect('profile')  # Перенаправляем пользователя на страницу профиля после создания заказа

            except Exception as e:
                return JsonResponse(
                    {'success': False, 'message': f'Ошибка: {str(e)}'})  # В случае ошибки возвращаем JSON-ответ

    return JsonResponse(
        {'success': False, 'message': 'Недопустимые данные формы.'})  # Возвращаем JSON-ответ при неверных данных формы
