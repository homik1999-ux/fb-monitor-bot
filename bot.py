import requests

TOKEN = "TU_WKLEJ_TOKEN"
CHAT_ID = "8664071476"

KEYWORDS = [
    "klimatyzacja",
    "montaż klimy",
    "klimatyzator",
    "pompa ciepła"
]

GROUPS = [
    "https://facebook.com/groups/TWOJA_GRUPA"
]


def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    requests.post(url, data=data)


send_telegram("Bot działa ✅ Sprawdzanie grup uruchomione.")
