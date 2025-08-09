import pytest
from aioresponses import aioresponses

from base.telegram_bot.tasks import \
    send_message_to_telegram  # Импортируйте вашу функцию


@pytest.mark.asyncio
async def test_send_message_to_telegram():
    with aioresponses() as m:
        m.post(
            "https://api.telegram.org/botTOKEN/sendMessage",
            payload={
                "ok": True,
                "result": {
                    "message_id": 123,
                    "chat": {"id": "CHAT_ID", "type": "private"},
                    "date": 1585893427,
                    "text": "Test message",
                },
            },
            status=200,
        )
        chat_id = "CHAT_ID"
        text = "Test message"
        token = "TOKEN"
        status, response_text = await send_message_to_telegram(chat_id, text, token)
        assert status == 200
