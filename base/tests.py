from django.test import TestCase
from base.form import BookingForm
import pytest
from django.utils import timezone
from django.contrib.auth.models import User
from base.models import Client, Booking, News

@pytest.mark.django_db
def test_client_model():
    client = Client.objects.create(name="John Doe", phone="1234567890")
    assert client.__str__() == "John Doe, 1234567890"

@pytest.mark.django_db
def test_booking_model():
    client = Client.objects.create(name="John Doe", phone="1234567890")
    booking = Booking.objects.create(client=client, name="John's Booking", phone="1234567890", date_in=timezone.now(), date_out=timezone.now(), guests=2, rooms=1)
    assert booking.client == client

@pytest.mark.django_db
def test_news_model():
    user = User.objects.create(username='user1')
    news = News.objects.create(title="Test News", content="This is a test news content", author=user)
    assert news.title == "Test News"


@pytest.mark.django_db
def test_booking_form():
    form_data = {'name': 'John Doe', 'phone': '1234567890', 'date_in': '2024-01-01', 'date_out': '2024-01-02', 'guests': 2, 'rooms': 1}
    form = BookingForm(data=form_data)
    assert form.is_valid()
    booking = form.save()
    assert booking.name == 'John Doe'

