from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['Сиф', 'Мускул', 'Ариэль']


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        name = form.data['username']
        password = form.data['password']
        password_repeat = form.data['repeat_password']
        age = form.data['age']
        flag = True
        error = ''

        if password_repeat != password:
            flag = False
            error = 'Пароли не совпадают'
        if int(age) < 18:
            flag = False
            error = 'Вы должны быть старше 18'
        if name in users:
            flag = False
            error = "Пользователь уже существует"
        info = {'form': form, 'error': error}
        if flag:
            return HttpResponse(f"Добро пожаловать, {name}")
        else:
            print(info)
            return render(request, 'registration_page.html', info)
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})


def sign_up_by_html(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        password_repeat = request.POST.get('repeat_password')
        age = request.POST.get('age')
        flag = True
        error = ''

        if password_repeat != password:
            flag = False
            error = 'Пароли не совпадают'
        if int(age) < 18:
            flag = False
            error = 'Вы должны быть старше 18'
        if name in users:
            flag = False
            error = "Пользователь уже существует"
        if flag:
            return HttpResponse(f"Добро пожаловать, {name}")
        else:
            info = {'error': error}
            return render(request, 'registration_page.html', info)

    return render(request, 'registration_page.html')
