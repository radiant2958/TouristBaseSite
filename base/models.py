from django.db import models



class Client(models.Model):
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Номер телефона', max_length=15)

    def __str__(self):
        return f"{self.name}, {self.phone}"


class Booking(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(verbose_name='Имя',max_length=100)
    phone = models.CharField(verbose_name='Номер телефона',max_length=15)
    date_in = models.DateField(verbose_name='Заезд')
    date_out = models.DateField(verbose_name='Выезд')
    GUEST_CHOICES = [(i, f"{i}" if i <= 5 else "6 и более человек") for i in range(1, 7)]
    guests = models.IntegerField(choices=GUEST_CHOICES, verbose_name='Количество гостей')
    ROOM_CHOICES = [(i, f"{i} дом{'а' if 2 <= i <= 4 else ''}") for i in range(1, 9)]
    rooms = models.IntegerField(choices=ROOM_CHOICES, verbose_name='Количество домов')
    is_processed = models.BooleanField(default=False, verbose_name='Обработана')

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Автор")


    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


