# edu/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.home, name='home'),
    # Страница со списком сортов мороженого
    path('profile/<str:username>/', views.profile, name='profile'),
    # Отдельная страница с информацией о сорте мороженого
    path('progress/<slug:subject>/<slug:group>/', views.progress),
]
