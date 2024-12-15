from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Пароль хэшируется в модели
            messages.success(request, "Registration successful!")
            return redirect('login')  # Перенаправляем на страницу входа
    else:
        form = RegistrationForm()

    return render(request, 'users/register.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']  # Получаем объект пользователя
            request.session['user_id'] = user.id  # Сохраняем ID пользователя в сессии
            messages.success(request, "Login successful!")
            return redirect('books:booklist')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})

def logout(request):
    """Выход из системы (удаление данных сессии пользователя)."""
    request.session.flush()  # Удаляем все данные сессии

    messages.success(request, "You have been logged out.")
    # Перенаправляем на главную страницу
    return redirect('books:booklist')  # Перенаправляем на страницу входа