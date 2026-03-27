import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

message = "🔥 تقرير اليوم جاهز"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

res = requests.post(url, json={
    "chat_id": CHAT_ID,
    "text": message
})

print(res.text)
