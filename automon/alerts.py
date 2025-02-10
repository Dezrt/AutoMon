import requests

TOKEN = "7721562129:AAGCPT2hB1Nn3wPJOHrvhl-uxgV6fXGWVz8"
CHAT_ID = "7721562129"

def send_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

if __name__ == "__main__":
    send_alert("🔥 AutoMon запущен! 🔥")
