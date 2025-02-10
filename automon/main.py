import psutil
import time

def monitor():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        print(f"CPU: {cpu}% | RAM: {ram}% | Disk: {disk}%")

        if cpu > 90:
            print("[ALERT] Высокая загрузка CPU!")
        if ram > 90:
            print("[ALERT] ОЗУ заканчивается!")

        time.sleep(5)  # Проверяем раз в 5 секунд

if __name__ == "__main__":
    monitor()
