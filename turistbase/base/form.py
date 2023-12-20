from django import forms
from .models import Booking, Client

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone', 'date_in', 'date_out', 'guests', 'rooms']
    
    def save(self, commit=True):
        client, created = Client.objects.get_or_create(
            name=self.cleaned_data['name'],
            phone=self.cleaned_data['phone']
        )

        booking = super(BookingForm, self).save(commit=False)
        booking.client = client

        if commit:
            booking.save()
        
        return booking
