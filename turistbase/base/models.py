from django.db import models



class Client(models.Model):
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Номер телефона', max_length=15)

    def __str__(self):
        return self.name, self.phone


class Booking(models.Model):
    name = models.CharField(verbose_name='Имя',max_length=100)
    phone = models.CharField(verbose_name='Номер телефона',max_length=15)
    date_in = models.DateField(verbose_name='Заезд')
    date_out = models.DateField(verbose_name='Выезд')
    GUEST_CHOICES = [(i, f"{i} гостя") for i in range(2, 5)]
    guests = models.IntegerField(choices=GUEST_CHOICES, verbose_name='Количество гостей')

    ROOM_CHOICES = [(i, f"{i} дом{'а' if 2 <= i <= 4 else ''}") for i in range(1, 8)]
    rooms = models.IntegerField(choices=ROOM_CHOICES, verbose_name='Количество домов')





