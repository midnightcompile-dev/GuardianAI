import psutil


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


cpu_usage = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage("/")
battery = psutil.sensors_battery()

gb = 1024 ** 3

print_header()

print(f"System Health : {system_health(cpu_usage, memory.percent)}")
print()

print(f"CPU Usage     : {cpu_usage}%")

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
    if battery.power_plugged:
        print("Status        : Charging 🔌")
    else:
        print("Status        : On Battery 🔋")
else:
    print("Battery information not available.")

print_footer()