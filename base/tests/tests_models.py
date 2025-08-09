from datetime import date, timedelta

import pytest
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.utils.timezone import now

from base.clients.views import check_client_exists, create_client
from base.models import Booking, Client, News


@pytest.mark.django_db
def test_client_creation():
    client = Client.objects.create(name="Иван Иванов", phone="1234567890")
    assert Client.objects.count() == 1
    assert str(client) == "Иван Иванов, 1234567890"


@pytest.mark.django_db
def test_client_unique_phone():
    Client.objects.create(name="Иван Иванов", phone="1234567890")
    with pytest.raises(IntegrityError):
        Client.objects.create(name="Петр Петров", phone="1234567890")


@pytest.mark.django_db
def test_news_creation():
    user = User.objects.create_user(username="testuser", password="12345")
    news = News.objects.create(
        title="Новость 1", content="Содержание новости 1", author=user
    )
    assert News.objects.count() == 1
    assert news.pub_date <= now()
    assert str(news) == "Новость 1"


@pytest.mark.django_db
def test_client_field_lengths():
    client = Client.objects.create(
        name="Имя" * 12, phone="1" * 15
    )  # Предполагая макс. длину name = 50, phone = 15
    assert len(client.name) <= 50
    assert len(client.phone) == 15


@pytest.mark.django_db
def test_booking_guests_and_rooms_choices():
    booking = Booking.objects.create(
        name="Тест",
        phone="123456789",
        date_in=date.today(),
        date_out=date.today() + timedelta(days=1),
        guests=2,
        rooms=3,
    )
    assert booking.guests in [choice[0] for choice in Booking.GUEST_CHOICES]
    assert booking.rooms in [choice[0] for choice in Booking.ROOM_CHOICES]


@pytest.mark.django_db
def test_news_authorship():
    user = User.objects.create_user(username="author", password="12345")
    news = News.objects.create(
        title="Тестовая новость", content="Тестовое содержание", author=user
    )
    assert news.author == user


@pytest.mark.django_db
def test_news_ordering():
    user = User.objects.create_user(username="author", password="12345")
    older_news = News.objects.create(
        title="Старая новость",
        content="Содержание старой новости",
        author=user,
        pub_date=now() - timedelta(days=1),
    )
    newer_news = News.objects.create(
        title="Новая новость",
        content="Содержание новой новости",
        author=user,
        pub_date=now(),
    )
    assert list(News.objects.all().order_by("pub_date")) == [older_news, newer_news]


@pytest.mark.django_db
def test_check_client_exists():
    Client.objects.create(name="Тестовый Клиент", phone="1234567890")

    assert check_client_exists("1234567890") == True
    assert check_client_exists("0987654321") == False


@pytest.mark.django_db
def test_create_client():
    response = create_client("Новый Клиент", "0987654321")
    assert Client.objects.filter(phone="0987654321").exists() == True
    assert response == "Новая заявка на бронирование.\n"

    response = create_client("Еще один Клиент", "0987654321")
    assert Client.objects.filter(phone="0987654321").count() == 1
    assert response == "Клиент с таким номером телефона уже существует в базе данных.\n"
