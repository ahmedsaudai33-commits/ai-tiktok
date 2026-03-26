import requests

message = "🔥 تقرير اليوم جاهز"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, json={
    "chat_id": CHAT_ID,
    "text": message
})
