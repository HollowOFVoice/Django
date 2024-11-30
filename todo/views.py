from django.shortcuts import render, redirect, get_object_or_404
from .models import Task  # Убедитесь, что у вас есть модель Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# В общем, как я понял здесь происходит обработка html страничка.
# Типо, происходит обработка различного рода действий например как здесь, в login_view
# Данный метод обрабатывает форму html после нажатия на кнопку отправки данных в форме
# Здесь применяется метод пост, из которого мы получаем данные и уже здесь в зависимости от того,
# Правильно или нет введены данные, и есть ли например пользователь в базе с таким логином и паролем
# сложно пипец, поэтому понятнее пока не скажу ㄟ( ▔, ▔ )ㄏ



def task_list(request):
    tasks = Task.objects.all()  # Получаем все задачи из базы данных
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Получаем задачу по ID

    if request.method == 'POST':
        task.delete()  # Удаляем задачу
        return redirect('tasks_list')  # Перенаправляем на список задач

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tasks_list')  # Перенаправление на страницу со списком задач
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
            return render(request, 'auth/login.html', {'error': 'Неверное имя пользователя или пароль.'})

    return render(request, 'todo/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Вход пользователя после регистрации
            return redirect('login')  # Перенаправление на страницу входа или другую страницу
    else:
        form = UserCreationForm()
    return render(request, 'todo/register.html', {'form': form})

# Create your views here.
