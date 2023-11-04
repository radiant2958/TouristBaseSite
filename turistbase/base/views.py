from django.shortcuts import render, redirect
from .form import BookingForm
from .models import Booking
from .telegram import send_message_to_telegram
import asyncio


TOKEN = '6412915643:AAG9-GnFuFc7O0FAj0n5rbMsy3pql7gw0lA'
# CHAT_ID = '627339615'

CHAT_ID = '-4037145215'


def index(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            name = form.cleaned_data.get('name')
            date_in = form.cleaned_data.get('date_in')
            date_out = form.cleaned_data.get('date_out')
            guests = form.cleaned_data.get('guests')
            rooms = form.cleaned_data.get('rooms')
            
            existing_booking = Booking.objects.filter(phone=phone).first()
            
            if existing_booking:
                message = f"Заявка на бронирование!\n" \
                          f"Пользователь с номером {phone} уже существует в базе данных!\n" \
                          f"Имя: {existing_booking.name}\n" \
                          f"Даты бронирования: с {existing_booking.date_in} по {existing_booking.date_out}\n" \
                          f"Количество гостей: {existing_booking.guests}\n" \
                          f"Количество домов: {existing_booking.rooms}"
            else:
                form.save()
                message = f"Новая заявка на бронирование\n" \
                          f"Телефон {phone}\n" \
                          f"Имя: {name}\n" \
                          f"Даты бронирования: с {date_in} по {date_out}\n" \
                          f"Количество гостей: {guests}\n" \
                          f"Количество домов: {rooms}"
            
            try:
                # Используйте асинхронный запуск для отправки сообщения в Telegram
                response_status, response_text = asyncio.run(send_message_to_telegram(CHAT_ID, message, TOKEN))
                print(f"Telegram API Response: Status - {response_status}, Text - {response_text}")
            except Exception as e:
                print(f"Error: {e}")
            
            return redirect('success_page')
    else:
        form = BookingForm()
    
    return render(request, 'base/index.html', {'form': form})


def about(request):
    return render(request,"base/about-us.html")

def contact(request):
    return render(request, "base/contact.html")

def new(request):
    return render(request, "base/blog.html")

def success_page(request):
    return render(request, 'base/success.html')


