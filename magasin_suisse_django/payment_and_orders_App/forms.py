from django import forms
from django.core.exceptions import ValidationError
import re
from django import forms
from .models import CustomerInfo

def validate_name(value):
    if not value.isalpha():
        raise ValidationError("Name can only contain letters.")

def validate_address(value):
    if not re.match(r'^[a-zA-Z0-9\s@#&.,_-]*$', value):
        raise ValidationError("Address contains invalid characters.")

def validate_postal_code(value):
    if not re.match(r'^\d{4}$', value):
        raise ValidationError("Postal code must contain exactly 4 digits.")

def validate_email(value):
    if not "@" in value:
        raise ValidationError("Invalid email format. Email must contain the @ symbol.")

class OrderForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        help_text='Enter the recipient\'s first name.',
        required=True,
        validators=[validate_name]
    )
    last_name = forms.CharField(
        label='Last Name',
        help_text='Enter the recipient\'s last name.',
        required=True,
        validators=[validate_name]
    )

    delivery_address = forms.CharField(
        label='Delivery Address',
        help_text='Specify the delivery address (street, house, apartment, etc.).',
        required=True,
        validators=[validate_address]
    )

    delivery_postal_code = forms.CharField(
        label='Postal Code',
        help_text='Specify the postal code.',
        required=True,
        validators=[validate_postal_code]
    )

    email = forms.EmailField(
        label='Email',
        help_text='Enter your email address.',
        validators=[validate_email]
    )

    notes = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Additional Notes'}),
        required=False,
        label='Order Notes',
        help_text='If you have any additional notes for the order, please enter them here.'
    )

class CustomerInfoForm(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = ['first_name', 'last_name', 'delivery_address', 'delivery_postal_code', 'email', 'notes']
