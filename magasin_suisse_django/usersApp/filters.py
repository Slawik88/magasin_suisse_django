import django_filters
from .models import CustomUser

class CustomUserFilter(django_filters.FilterSet):
    class Meta:
        model = CustomUser
        fields = {
            'is_staff': ['exact'],
            'is_active': ['exact'],
            'username': ['icontains'],
        }
