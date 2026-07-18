def analyze_system(cpu, ram, disk):
    if cpu > 80:
        return "⚠️ CPU usage is very high."

    if ram > 90:
        return "⚠️ RAM usage is very high."

    if disk > 95:
        return "⚠️ Disk is almost full."

    return "✅ System is operating normally."
