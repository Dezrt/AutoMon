import os
import psutil
import time

CRITICAL_SERVICES = ["nginx", "mysql", "docker"]

def restart_service(service):
    print(f"[FIX] Перезапуск {service}...")
    os.system(f"sudo systemctl restart {service}")

def check_services():
    for service in CRITICAL_SERVICES:
        if service not in (p.name() for p in psutil.process_iter()):
            print(f"[ALERT] {service} упал! Перезапускаем...")
            restart_service(service)

if __name__ == "__main__":
    while True:
        check_services()
        time.sleep(10)
