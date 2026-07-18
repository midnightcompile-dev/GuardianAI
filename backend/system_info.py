import psutil

cpu_usage = psutil.cpu_percent(interval=1)

print("========== GuardianAI ==========")
print(f"CPU Usage : {cpu_usage}%")
print("================================")