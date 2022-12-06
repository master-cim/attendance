from django.apps import AppConfig


class EduConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'edu'
     # под этим именем приложение будет видно в админке.
    verbose_name = 'Журнал учета посещаемости и успеваемости занятий' 
