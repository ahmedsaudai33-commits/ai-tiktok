import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

message = """
🔥 فكرة اليوم

🎯 العنوان:
كيف تجيب مشاهدات عالية؟

🧠 الهوك:
في حركة بسيطة تخلي الفيديو ينفجر

📹 الفكرة:
ابدأ بمشهد قوي + سؤال يخلّي الناس تكمل

📊 الهدف:
رفع المشاهدات والمتابعين
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

res = requests.post(url, json={
    "chat_id": CHAT_ID,
    "text": message
})

print(res.text)
