import requests
import feedparser
import json
import os
print("START BOTA", flush=True)
TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = "8664071476"
RSS_FEEDS = [
    "https://rss.app/feeds/EYUXQBM0N6GWpF1X.xml","https://rss.app/feeds/aeBHmOEXiFgcpoRn.xml","https://rss.app/feeds/2xT8AdXui6fknvR4.xml","https://rss.app/feeds/pPYNvbbRwQkSGdru.xml",
]
KEYWORDS = [
    # === MITSUBISHI ELECTRIC - serie ścienne ===
    "mitsubishi hr", "mitsubishi ap", "mitsubishi ay", "mitsubishi ln",
    "mitsubishi ef", "mitsubishi slz", "mitsubishi mlz", "mitsubishi mfz",
    "mitsubishi sez", "mitsubishi suz", "mitsubishi ft", "mitsubishi rw",
    "mitsubishi mxz", "msz-hr", "msz-ap", "msz-ay", "msz-ln", "msz-ef",
    "muz-hr", "muz-ap", "muz-ay", "muz-ln", "muz-ef",
    # Mitsubishi - technologie
    "mitsubishi zubadan", "mitsubishi hyper heating",
    "zubadan", "hyper heating",
    # Mitsubishi - pompy ciepła
    "ecodan", "mitsubishi ecodan",
    "mitsubishi mr.slim", "mr slim mitsubishi", "mr.slim",
    # Mitsubishi - multisplit
    "mitsubishi mxz", "mxz mitsubishi", "mitsubishi multi",
    "mitsubishi multisplit", "agregat mitsubishi multi",

    # === DAIKIN - serie ścienne ===
    "daikin sensira", "daikin perfera", "daikin comfora", "daikin stylish",
    "daikin emura", "daikin ururu", "daikin sarara", "daikin ftxz",
    "sensira daikin", "perfera daikin", "comfora daikin", "stylish daikin",
    "emura daikin", "ururu sarara",
    # Daikin - kody modeli
    "ftxm daikin", "ftxa daikin", "ftxp daikin", "ftxj daikin",
    "rxm daikin", "rxa daikin", "rxp daikin", "rxj daikin",
    # Daikin - multisplit
    "daikin multi", "daikin multisplit", "agregat daikin multi",
    "daikin 2mxm", "daikin 3mxm", "daikin 4mxm", "daikin 5mxm",
    # Daikin - pompy ciepła
    "daikin altherma", "altherma daikin", "altherma",
    # Daikin - technologie
    "daikin bluevolution", "daikin nepura", "nepura daikin",
    "daikin siesta", "sensira siesta",
    # Daikin - VRV
    "daikin vrv", "vrv daikin",

    # === TOSHIBA - serie ścienne ===
    "toshiba seiya", "toshiba shorai", "toshiba daiseikai", "toshiba haori",
    "seiya toshiba", "shorai toshiba", "daiseikai toshiba", "haori toshiba",
    "toshiba shorai edge", "shorai edge", "shorai edge toshiba",
    "toshiba suzumi", "suzumi toshiba",
    "toshiba seiya classic", "seiya classic",
    "toshiba daiseikai 10", "daiseikai 10",
    # Toshiba - multisplit
    "toshiba multi", "toshiba multisplit", "agregat toshiba multi",
    "toshiba ras", "ras-b toshiba",
    # Toshiba - pompy ciepła
    "toshiba estia", "estia toshiba", "estia",

    # === OGÓLNE nazwy marek (jako backup) ===
    "mitsubishi electric", "mitsubishi",
    "daikin",
    "toshiba hvac", "toshiba",
]
SEEN_FILE = "seen_posts.json"
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
            print(f"Wysłano: {matched_kw}", flush=True)
all_seen = seen | new_seen
if len(all_seen) > 500:
    all_seen = new_seen
save_seen(all_seen)
print(f"Znaleziono dopasowań: {found_count}", flush=True)
print("KONIEC BOTA", flush=True)
