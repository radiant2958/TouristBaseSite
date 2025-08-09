from unittest.mock import patch

import pytest
from django.test import Client
from django.urls import reverse


@pytest.fixture
def client():
    return Client()


@pytest.mark.asyncio
def test_bad_request_error(client):
    response = client.post(reverse("error400"), data={})
    assert response.status_code == 400
