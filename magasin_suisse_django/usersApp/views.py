from django.contrib.auth import login, logout
from django.shortcuts import redirect

from .forms import CustomUserCreationForm, UserProfileForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usersApp/register.html', {'form': form})


def profile(request):
    user = request.user  # Получаем объект пользователя текущей сессии
    return render(request, 'usersApp/profile.html', {'user': user})


def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()  # Update the user's data
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'usersApp/edit_profile.html', {'form': form})


from django.contrib.auth.views import LoginView
from django.shortcuts import render


def login_view(request):
    response = LoginView.as_view(
        template_name='usersApp/login.html',  # Ваш собственный шаблон
        extra_context={'registration_link': '/registration/'}
    )(request)

    if request.user.is_authenticated:
        # Если пользователь успешно вошел, перенаправьте его на домашнюю страницу (замените 'home' на ваш URL-шаблон домашней страницы)
        return redirect('home')

    return response


def logout_view(request):
    logout(request)
    return redirect('profile')
