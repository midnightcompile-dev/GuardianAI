import time
from collectors.system_collector import get_system_info

while True:
    data = get_system_info()

    cpu = data["cpu"]
    memory = data["memory"]
    disk = data["disk"]

    print("\n" * 5)
    print("🛡️ GuardianAI Live Monitor")
    print("=" * 40)

    print(f"CPU Usage : {cpu}%")
    print(f"RAM Usage : {memory.percent}%")
    print(f"Disk Usage: {disk.percent}%")

    print("=" * 40)

    time.sleep(2)
    