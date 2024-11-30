from django.urls import path
from .views import task_list, login_view, register_view, delete_task

# ЕСЛИ ПРАВИЛЬНО ПОНЯЛ, ТО ЗДЕСЬ СОЗДАЕТСЯ ССЫЛКА НА ФАЙЛ VIEWS.PY, В КОТОРОМ ПРОИСХОДИТ ВЫЗОВ HTML ФАЙЛА
# И ДОП ШТУКИ ДЛЯ НЕГО. в ТЕКУЩЕМ ФАЙЛЕ МЫ ВЫЗЫВАЕМ TASK_LIST И ДАЁМ ЕМУ ИМЯ ПО КОТОРОМУ МЫ ВЫХЫВАЕМ ЕГО В
# ПАПКЕ КОНФИГ ГДЕ ЕСТЬ ТАКОЙ ЖЕ ФАЙЛ URLS
urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('tasks/delete/<int:task_id>/', delete_task, name='delete_task'),
    path('tasks/', task_list, name='tasks_list'),

]
