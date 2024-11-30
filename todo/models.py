from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
# КАК Я ПОНЛЯ СОДЕЛИ ЭТО ПО СУТИ ТАБЛИЦА В БД, В КОТОРУЮ ВХОДЯТ ОПРЕДЕЛЕННЫЕ ПАРАМЕТРЫ ПО ТИПУ
    # пОЛЬЗОВААТЕЛЬ ФИО, НОМЕР ТЕЛЕФОНА, ДАТА РОЖДЕНИЯ
    def __str__(self):
        return self.title

# Create your models here.
