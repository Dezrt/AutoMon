import requests

TOKEN = ""
CHAT_ID = ""

def send_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

if __name__ == "__main__":
    send_alert("🔥 AutoMon запущен! 🔥")
