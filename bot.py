
print("START SKRYPTU")

import requests
TOKEN = "8745828890:AAFx0jw6fNFTLmuVZLD211oq0nZ8bbTrQw0"
CHAT_ID = "8664071476"

print("Wysyłam wiadomość...")

requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": "Test z GitHub Actions ✅"}
)

print("KONIEC SKRYPTU")
