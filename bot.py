import requests

TOKEN = "8745828890:AAFx0jw6fNFTLmuVZLD211oq0nZ8bbTrQw0"
CHAT_ID = "8664071476"


def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    requests.post(url, data=data)


send_telegram("Bot działa poprawnie ✅ GitHub wysłał wiadomość.")
