from django.contrib.auth import views as auth_views
from django.urls import path

from usersApp import views
from usersApp.views import login_view

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Другие URL-маршруты вашего приложения
]