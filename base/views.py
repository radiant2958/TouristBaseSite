import asyncio
import os

from django.contrib import messages
from django.shortcuts import redirect, render
from dotenv import load_dotenv

from base.bookings.forms import BookingForm
from base.models import News
from base.telegram_bot.tasks import send_message_to_telegram

from .bookings.views import format_booking_message
from .clients import views

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def index(request):
    return render(request, "base/index.html")


def title_base(request):
    if request.method == "POST":
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            first_part_message = views.create_client(booking.name, booking.phone)
            second_part_message = format_booking_message(booking)
            final_message = first_part_message + second_part_message

            booking.save()
            try:
                asyncio.run(send_message_to_telegram(CHAT_ID, final_message, TOKEN))
                messages.success(request, "Бронирование успешно создано и сообщение отправлено.")
            except Exception as e:
                messages.error(request, f"Ошибка при отправке сообщения: {e}")

            return redirect("success_page")
        else:
            redirect("handler400")
    else:
        booking_form = BookingForm()

    return render(request, "base/title_base.html", {"form": booking_form})


def about(request):
    return render(request, "base/about-us.html")


def contact(request):
    return render(request, "base/contact.html")


def new(request):
    news_list = News.objects.all().order_by("-pub_date")
    return render(request, "base/blog.html", {"news_list": news_list})


def success_page(request):
    return render(request, "base/success.html")


def room(request):
    return render(request, "base/room.html")


def roomZero(request):
    return render(request, "base/room-details.html")


def roomOne(request):
    return render(request, "base/room1-details.html")


def roomSecond(request):
    return render(request, "base/room2-details.html")


def roomThird(request):
    return render(request, "base/room3-details.html")


def roomFourth(request):
    return render(request, "base/room4-details.html")


def roomsTriple(request):
    return render(request, "base/room5-details.html")


def handler400(request, exception):
    return render(request, "base/errors/400.html", status=400)


def handler500(request):
    response = render(request, "base/errors/500.html", {})
    response.status_code = 500
    return response
