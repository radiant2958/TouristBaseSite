from django.shortcuts import render, redirect
from .form import BookingForm
from .models import Booking, Client, News
from .telegram import send_message_to_telegram
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()  

TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


def index(request):
    return render(request, 'base/index.html')



def title_base(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            
            message = f"Новая заявка на бронирование\n" \
                      f"Телефон: {booking.client.phone}\n" \
                      f"Имя: {booking.client.name}\n" \
                      f"Даты бронирования: с {booking.date_in} по {booking.date_out}\n" \
                      f"Количество гостей: {booking.guests}\n" \
                      f"Количество домов: {booking.rooms}"

            phone = form.cleaned_data.get('phone')
            name = form.cleaned_data.get('name')
            date_in = form.cleaned_data.get('date_in')
            date_out = form.cleaned_data.get('date_out')
            guests = form.cleaned_data.get('guests')
            rooms = form.cleaned_data.get('rooms')
            
            client, created = Client.objects.get_or_create(
                phone=phone, defaults={'name': name}
            )
            if not created:
                message = f"Новая заявка на бронирование\n" \
                          f"Телефон {phone}\n" \
                          f"Имя: {name}\n" \
                          f"Даты бронирования: с {date_in} по {date_out}\n" \
                          f"Количество гостей: {guests}\n" \
                          f"Количество домов: {rooms}"
               
            else:
                form.save()
                message = f"Заявка на бронирование!\n" \
                          f"Пользователь с номером {phone} уже существует в базе данных!\n" \
                          f"Имя: {client.name}\n" \
                          f"Даты бронирования: с {date_in} по {date_out}\n" \
                          f"Количество гостей: {guests}\n" \
                          f"Количество домов: {rooms}"
            
            try:
        
                response_status, response_text = asyncio.run(send_message_to_telegram(CHAT_ID, message, TOKEN))
                print(f"Telegram API Response: Status - {response_status}, Text - {response_text}")
            except Exception as e:
                print(f"Error: {e}")
            
            return redirect('success_page')
    else:
        form = BookingForm()
    
    return render(request, 'base/title_base.html', {'form': form})


def about(request):
    return render(request,"base/about-us.html")

def contact(request):
    return render(request, "base/contact.html")

def new(request):
    news_list = News.objects.all().order_by('-pub_date')  
    return render(request, "base/blog.html", {'news_list': news_list})

def success_page(request):
    return render(request, 'base/success.html')

def room(request):
    return render(request, "base/room.html")

def roomZero(request):
    return render(request, "base/room-details.html")

def roomOne(request):
    return render(request, "base/room1-details.html")

def roomSecond(request):
    return render(request, 'base/room2-details.html')

def roomThird(request):
    return render(request, "base/room3-details.html")

def roomFourth(request):
    return render(request, "base/room4-details.html")

def roomsTriple(request):
    return render(request, 'base/room5-details.html')

