import aiohttp


async def send_message_to_telegram(chat_id, text, token):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload) as response:
            response_text = await response.text()
            if response.status != 200:
                print(
                    f"Failed to send message. Status: {response.status}. Response: {response_text}"
                )
            return response.status, response_text
