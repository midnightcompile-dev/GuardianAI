from collectors.system_collector import get_system_info


def print_header():
    print("🛡️ GuardianAI - System Monitor")
    print("=" * 40)


def print_footer():
    print("=" * 40)


def system_health(cpu, ram):
    if cpu < 50 and ram < 70:
        return "🟢 Good"
    elif cpu < 80 and ram < 90:
        return "🟡 Moderate"
    else:
        return "🔴 High Resource Usage"


data = get_system_info()

cpu = data["cpu"]
memory = data["memory"]
disk = data["disk"]
battery = data["battery"]
gb = data["gb"]

print_header()

print(f"System Health : {system_health(cpu, memory.percent)}")
print()

print(f"CPU Usage     : {cpu}%")

print(f"Total RAM     : {memory.total / gb:.2f} GB")
print(f"Used RAM      : {memory.used / gb:.2f} GB")
print(f"Available RAM : {memory.available / gb:.2f} GB")
print(f"RAM Usage     : {memory.percent}%")

print()

print(f"Disk Total    : {disk.total / gb:.2f} GB")
print(f"Disk Used     : {disk.used / gb:.2f} GB")
print(f"Disk Free     : {disk.free / gb:.2f} GB")
print(f"Disk Usage    : {disk.percent}%")

print()

if battery:
    print(f"Battery       : {battery.percent}%")
    print("Status        : Charging 🔌" if battery.power_plugged else "Status        : On Battery 🔋")
else:
    print("Battery information not available.")

print_footer()