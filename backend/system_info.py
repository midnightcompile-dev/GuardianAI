from collectors.system_collector import get_system_info
from analyzer.system_analyzer import analyze_system


def print_header():
    print("🛡️ GuardianAI - System Monitor")
    print("=" * 40)


def print_footer():
    print("=" * 40)


data = get_system_info()

cpu = data["cpu"]
memory = data["memory"]
disk = data["disk"]
battery = data["battery"]
gb = data["gb"]

health = analyze_system(cpu, memory.percent, disk.percent)

print_header()

print(health)
print()

print(f"CPU Usage     : {cpu}%")
print(f"RAM Usage     : {memory.percent}%")
print(f"Disk Usage    : {disk.percent}%")

if battery:
    print(f"Battery       : {battery.percent}%")

print_footer()