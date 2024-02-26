import pytest
from django.contrib.auth.models import User
from datetime import date, timedelta
from base.bookings.forms import BookingForm
from base.news.forms import NewsForm
from django.core.exceptions import ValidationError

@pytest.mark.django_db
def test_news_form_valid():
    user = User.objects.create(username='testuser', password='12345')
    form_data = {'title': 'Test Title', 'content': 'Test Content', 'author': user.id}
    form = NewsForm(data=form_data)
    assert form.is_valid()

@pytest.mark.django_db
def test_news_form_invalid():
    form_data = {'title': '', 'content': '', 'author': None}
    form = NewsForm(data=form_data)
    assert not form.is_valid()
    assert 'title' in form.errors
    assert 'content' in form.errors
    assert 'author' in form.errors


@pytest.mark.django_db
def test_booking_form_valid():
    form_data = {
        'name': 'Test Name',
        'phone': '+71234567890',
        'date_in': date.today(),
        'date_out': date.today() + timedelta(days=1),
        'guests': 1,
        'rooms': 1
    }
    form = BookingForm(data=form_data)
    assert form.is_valid()

@pytest.mark.django_db
def test_booking_form_invalid_dates():
    form_data = {
        'name': 'Test Name',
        'phone': '+71234567890',
        'date_in': date.today() + timedelta(days=1),
        'date_out': date.today(),
        'guests': 1,
        'rooms': 1
    }
    form = BookingForm(data=form_data)
    assert not form.is_valid()
    assert 'Дата заезда должна быть раньше даты выезда.' in str(form.errors)

@pytest.mark.django_db
def test_booking_form_invalid_phone():
    form_data = {
        'name': 'Test Name',
        'phone': '12345',
        'date_in': date.today(),
        'date_out': date.today() + timedelta(days=1),
        'guests': 1,
        'rooms': 1
    }
    form = BookingForm(data=form_data)
    assert not form.is_valid()
    assert 'Введите корректный номер телефона, начинающийся с +7 или 8 и содержащий 11 цифр.' in str(form.errors)

@pytest.mark.django_db
def test_booking_form_save_with_missing_fields():
    # Подготавливаем данные формы с намеренно пропущенными обязательными полями
    form_data = {
        'name': 'Test Name',  # Предположим, что другие обязательные поля отсутствуют
       
    }
    form = BookingForm(data=form_data)
    
    # Даже если форма невалидна, пытаемся вызвать save() напрямую для тестирования
    if not form.is_valid():
        with pytest.raises(ValidationError) as excinfo:
            form.save()
        
        # Проверяем, содержит ли сообщение об ошибке упоминание о недостающих полях
        assert "Следующие поля обязательны к заполнению:" in str(excinfo.value)