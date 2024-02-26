from base.models import Client
from django.contrib import messages

def check_client_exists(phone):
    return Client.objects.filter(phone=phone).exists()

def create_client(name, phone):
    message1 = ""
    if not Client.objects.filter(phone=phone).exists():
        Client.objects.create(name=name, phone=phone)
        message1 = "Новая заявка на бронирование.\n"
    else:
        message1 = "Клиент с таким номером телефона уже существует в базе данных.\n"
    return message1
