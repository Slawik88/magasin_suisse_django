from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        pass

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперкористувач повинен мати is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперкористувач повинен мати is_superuser=True')

        return self._create_user(username, password, **extra_fields)

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('Поле "Ім\'я користувача" повинно бути заповненим')
        username = self.normalize_email(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Електронна пошта')
    username = models.CharField(max_length=150, unique=True, blank=True, verbose_name='Ім\'я користувача')
    first_name = models.CharField(max_length=150, blank=True, verbose_name='Ім\'я')
    last_name = models.CharField(max_length=150, blank=True, verbose_name='Прізвище')
    phone_number = models.CharField(max_length=20, blank=True, verbose_name='Номер телефону')
    shipping_address = models.CharField(max_length=255, blank=True, verbose_name='Адреса доставки')
    postal_code = models.CharField(max_length=4, blank=True, null=True, default='0000', verbose_name='Поштовий індекс')
    is_active = models.BooleanField(default=True, verbose_name='Активний')
    is_staff = models.BooleanField(default=False, verbose_name='Персонал')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Дата реєстрації')

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
