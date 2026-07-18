import psutil

memory = psutil.virtual_memory()

gb = 1024 ** 3

print("🛡️ GuardianAI - System Monitor")
print("=" * 40)

print(f"Total RAM     : {memory.total / gb:.2f} GB")
print(f"Used RAM      : {memory.used / gb:.2f} GB")
print(f"Available RAM : {memory.available / gb:.2f} GB")
print(f"RAM Usage     : {memory.percent}%")

print("=" * 40)