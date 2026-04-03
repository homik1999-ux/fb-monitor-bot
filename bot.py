import requests

print("START")

TOKEN = "TWÓJ_TOKEN"
CHAT_ID = "8664071476"

response = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": "Test z GitHub Actions ✅"}
)

print(response.text)
print("KONIEC")
