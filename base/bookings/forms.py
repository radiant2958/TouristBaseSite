from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from base.models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["name", "phone", "date_in", "date_out", "guests", "rooms"]

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if not (phone.startswith("+7") or phone.startswith("8")) or len(phone) != 12:
            raise ValidationError(
                "Введите корректный номер телефона, начинающийся с +7 или 8 и содержащий 11 цифр."
            )
        return phone

    def clean(self):
        cleaned_data = super().clean()
        date_in = cleaned_data.get("date_in")
        date_out = cleaned_data.get("date_out")

        if date_in and date_out and date_in > date_out:
            raise ValidationError("Дата заезда должна быть раньше даты выезда.")

        return cleaned_data

    def save(self, commit=True):
        mandatory_fields = ["name", "phone", "date_in", "date_out", "guests", "rooms"]
        missing_fields = [
            field for field in mandatory_fields if not self.cleaned_data.get(field)
        ]
        if missing_fields:
            error_message = _("Следующие поля обязательны к заполнению: ") + ", ".join(
                missing_fields
            )
            raise ValidationError(error_message)

        booking = super().save(commit=False)
        if commit:
            booking.save()
        return booking
