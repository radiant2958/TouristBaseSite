
from django.shortcuts import render, redirect
from .forms import BookingForm



def format_booking_message(booking):
    return (
        f"Имя: {booking.name}\n"
        f"Телефон: {booking.phone}\n"
        f"Даты бронирования: с {booking.date_in} по {booking.date_out}\n"
        f"Количество гостей: {booking.guests}\n"
        f"Количество домов: {booking.rooms}"
    )
