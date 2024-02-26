import pytest
from django.urls import reverse
from django.test import Client



@pytest.fixture
def client():
    return Client()

@pytest.mark.django_db
def test_index_page(client):
    url = reverse('title_base')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_about_page(client):
    url = reverse('about-us')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_room_page(client):
    url = reverse('room')  
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_roomZero_page(client):
    url = reverse('roomZero')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_room_second(client):
    url = reverse('roomSecond')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_contact(client):
    url = reverse('contact')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_new(client):
    url = reverse('new')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_success_page(client):
    response = client.get(reverse('success_page'))
    assert response.status_code == 200
    assert 'base/success.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_room_one(client):
    response = client.get(reverse('roomOne'))  
    assert response.status_code == 200
    assert 'base/room1-details.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_room_third(client):
    response = client.get(reverse('roomThird')) 
    assert response.status_code == 200
    assert 'base/room3-details.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_room_fourth(client):
    response = client.get(reverse('roomFourth'))  
    assert response.status_code == 200
    assert 'base/room4-details.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_rooms_triple(client):
    response = client.get(reverse('roomsTriple')) 
    assert response.status_code == 200
    assert 'base/room5-details.html' in [t.name for t in response.templates]

