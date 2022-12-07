# edu/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page


# для кеширования работы view-функции можно применить специальный декоратор
# Главная страница
@cache_page(60 * 15)
def home(request):
    return HttpResponse('Главная страница')


# Страница преподавателя с расписанием на сегодня
def profile(request, username):
    # Здесь код запроса к модели и создание словаря контекста
    # context = {
    #     
    # }
    # return render(request, 'edu/profile.html', context)
    return HttpResponse(f'Профиль преподавателя {username}')


# Страница журнал посещвемости и успеваемости одной дисциплины;
# view-функция принимает параметр pk из path()
def progress(request, subject, group):
    return HttpResponse(f'Дисциплина {subject}, {group}')
