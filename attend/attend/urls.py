"""attend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Eсли на сервер пришёл любой запрос (''),
    # перейди в файл urls приложения edu
    # и проверь там все path() на совпадение с запрошенным URL
    path('', include('edu.urls')),
    # Если в приложении edu не найдётся совпадений -
    # Django продолжит искать совпадения здесь, в головном файле urls.py.

    # Встроенная админка Django подключена «из коробки» по адресу admin/
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
