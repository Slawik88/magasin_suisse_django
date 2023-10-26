from django.urls import path

from . import views

urlpatterns = [
    path('payment-form/', views.order_and_payment, name='payment_form'),
    path('payment-form/success', views.save_order, name='payment_form_success')
]
