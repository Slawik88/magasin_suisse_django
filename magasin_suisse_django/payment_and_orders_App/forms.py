from django import forms
from django.core.exceptions import ValidationError
import re
from django import forms
from .models import CustomerInfo

def validate_name(value):
    if not value.isalpha():
        raise ValidationError("Имя может содержать только буквы.")

def validate_address(value):
    if not re.match(r'^[a-zA-Z0-9\s@#&.,_-]*$', value):
        raise ValidationError("Адрес содержит недопустимые символы.")

def validate_postal_code(value):
    if not re.match(r'^\d{4}$', value):
        raise ValidationError("Почтовый индекс должен содержать ровно 4 цифры.")

def validate_email(value):
    if not "@" in value:
        raise ValidationError("Неверный формат email. Email должен содержать символ @.")

class OrderForm(forms.Form):
    first_name = forms.CharField(
        label='Имя',
        help_text='Введите имя получателя.',
        required=True,
        validators=[validate_name]
    )
    last_name = forms.CharField(
        label='Фамилия',
        help_text='Введите фамилию получателя.',
        required=True,
        validators=[validate_name]
    )

    delivery_address = forms.CharField(
        label='Адрес доставки',
        help_text='Укажите адрес доставки (улица, дом, квартира и др.).',
        required=True,
        validators=[validate_address]
    )

    delivery_postal_code = forms.CharField(
        label='Почтовый индекс',
        help_text='Укажите почтовый индекс.',
        required=True,
        validators=[validate_postal_code]
    )

    email = forms.EmailField(
        label='Email',
        help_text='Укажите ваш адрес электронной почты.',
        validators=[validate_email]
    )

    notes = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Дополнительные примечания'}),
        required=False,
        label='Примечания к заказу',
        help_text='Если есть какие-либо дополнительные замечания к заказу, укажите их здесь.'
    )


class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = ['first_name', 'last_name', 'delivery_address', 'delivery_postal_code', 'email', 'notes']