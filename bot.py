
import requests
import feedparser
import json
import os
from datetime import datetime

print("START BOTA", flush=True)

# ============ KONFIGURACJA ============
TOKEN = os.environ["8745828890:AAFx0jw6fNFTLmuVZLD211oq0nZ8bbTrQw0"]
CHAT_ID = "8664071476"

RSS_FEEDS = [
    "https://rss.app/feeds/EYUXQBM0N6GWpF1X.xml",
]

KEYWORDS = [
    "mitsubishi hr","mitsubishi ap","mitsubishi ay","mitsubishi ln",
    "mitsubishi ef","mitsubishi slz","mitsubishi mlz","mitsubishi mfz",
    "mitsubishi sez","mitsubishi suz","mitsubishi ft","mitsubishi rw",
    "mitsubishi mxz","mitsubishi zubadan","mitsubishi hyper heating",
    "zubadan","hyper heating",
    "daikin sensira","daikin perfera","daikin comfora","daikin stylish",
    "sensira daikin","perfera daikin","comfora daikin","stylish daikin",
    "daikin multi","daikin multisplit","agregat daikin multi",
    "toshiba seiya","toshiba shorai","toshiba daiseikai","toshiba haori",
    "seiya toshiba","shorai toshiba","daiseikai toshiba","haori toshiba",
    "toshiba multi","toshiba multisplit","agregat toshiba multi"
]

SEEN_FILE = "seen_posts.json"
# ======================================

def load_seen():
    if os.path.exists(SEEN_FILE):
        with open(SEEN_FILE, "r") as f:
            return set(json.load(f))
    return set()

def save_seen(seen):
    with open(SEEN_FILE, "w") as f:
        json.dump(list(seen), f)

def send_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }, timeout=10)
    print("Telegram status:", response.status_code, flush=True)

def check_keywords(text):
    text_lower = text.lower()
    for kw in KEYWORDS:
        if kw.lower() in text_lower:
            return kw
    return None

# ============ GŁÓWNA LOGIKA ============
seen = load_seen()
new_seen = set()
found_count = 0

for feed_url in RSS_FEEDS:
    print(f"Sprawdzam: {feed_url}", flush=True)
    feed = feedparser.parse(feed_url)
    print(f"Liczba postów w feedzie: {len(feed.entries)}", flush=True)

    for entry in feed.entries:
        post_id = entry.get("id", entry.get("link", ""))
        title = entry.get("title", "")
        summary = entry.get("summary", "")
        link = entry.get("link", "")
        full_text = f"{title} {summary}"

        new_seen.add(post_id)

        if post_id in seen:
            continue

        matched_kw = check_keywords(full_text)
        if matched_kw:
            found_count += 1
            msg = (
                f"🔔 <b>Znaleziono: {matched_kw}</b>\n\n"
                f"📝 {title}\n\n"
                f"🔗 {link}"
            )
            send_telegram(msg)
            print(f"Wysłano powiadomienie: {matched_kw}", flush=True)

# Zapisz tylko nowe posty (max 500 żeby plik nie rósł w nieskończoność)
all_seen = (seen | new_seen)
if len(all_seen) > 500:
    all_seen = new_seen  # reset do tylko aktualnych
save_seen(all_seen)

print(f"Znaleziono dopasowań: {found_count}", flush=True)
print("KONIEC BOTA", flush=True)
