from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'date_in', 'date_out', 'guests', 'rooms']
