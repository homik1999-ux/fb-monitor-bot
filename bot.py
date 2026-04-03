import requests

TOKEN = "8745828890:AAH1yLOCo4Yksy6a9mFhpGxUt6LZQoEohIk"
CHAT_ID = "8664071476"

KEYWORDS = [
    "klimatyzacja",
    "montaż klimy",
    "klimatyzator",
    "pompa ciepła"
]

GROUPS = [
    "https://www.facebook.com/groups/983446936989580"
]


def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    requests.post(url, data=data)


send_telegram("Bot działa ✅ Sprawdzanie grup uruchomione.")
