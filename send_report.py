import os
import requests

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

prompt = """
أعطني فكرة تيك توك قوية وقصيرة بهذا الشكل:

🔥 فكرة اليوم
🎯 العنوان:
🧠 الهوك:
📹 السكربت:
🎬 طريقة التصوير:
🏷️ هاشتاقات:

اجعلها جذابة ومناسبة للترند.
"""

res = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    },
    json={
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.9
    }
)

data = res.json()

print(data)

if "choices" in data:
    message = data["choices"][0]["message"]["content"]
else:
    message = "❌ فيه مشكلة في API: " + str(data)

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, json={
    "chat_id": CHAT_ID,
    "text": message
})
