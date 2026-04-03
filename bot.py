import requests

print("START")

TOKEN = "8745828890:AAH1yLOCo4Yksy6a9mFhpGxUt6LZQoEohIk"
CHAT_ID = "8664071476"

response = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": "Test z GitHub Actions ✅"}
)

print(response.text)
print("KONIEC")
