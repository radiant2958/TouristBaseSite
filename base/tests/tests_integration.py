import asyncio
# Использование AsyncMock для асинхронного мокирования
from unittest.mock import AsyncMock, patch

import pytest
from asgiref.sync import sync_to_async
from django.contrib.messages import get_messages
from django.test import Client
from django.urls import reverse

from base.telegram_bot.tasks import send_message_to_telegram


@pytest.mark.django_db
async def test_booking_form_submission_and_message_sending():
    client = Client()
    url = reverse("title_base")

    form_data = {
        "name": "Test Name",
        "phone": "+71234567890",
        "date_in": "2023-01-01",
        "date_out": "2023-01-02",
        "guests": 1,
        "rooms": 1,
    }

    with patch(
        "base.telegram_bot.tasks.send_message_to_telegram", new_callable=AsyncMock
    ) as mock_send:
        mock_send.return_value = asyncio.Future()
        mock_send.return_value.set_result((200, "OK"))

        response = await sync_to_async(client.post)(url, form_data)

        mock_send.assert_called_once()

        assert response.status_code == 302
        assert response.url == reverse("success_page")

        messages = list(get_messages(response.wsgi_request))
        assert len(messages) > 0
        assert (
            str(messages[0]) == "Бронирование успешно создано и сообщение отправлено."
        )
