import requests

print("START SKRYPTU")

TOKEN = "8745828890:AAFx0jw6fNFTLmuVZLD211oq0nZ8bbTrQw0"
CHAT_ID = "8664071476"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": "Test z GitHub Actions ✅"
    }
)

print("STATUS:", response.status_code)
print("ODPOWIEDŹ:", response.text)

print("KONIEC SKRYPTU")
