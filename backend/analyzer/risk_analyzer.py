from database.trusted_processes import TRUSTED_PROCESSES


def calculate_risk(process):
    score = 0
    reasons = []

    name = (process["name"] or "").lower()
    path = (process["exe"] or "").lower()
    cpu = process["cpu_percent"] or 0
    ram = process["memory_percent"] or 0

    if name in TRUSTED_PROCESSES:
        reasons.append("Known trusted process")
    else:
        score += 25
        reasons.append("Unknown process")

    if "downloads" in path:
        score += 40
        reasons.append("Running from Downloads")

    elif "temp" in path:
        score += 50
        reasons.append("Running from Temp")

    elif "windows" in path:
        reasons.append("Windows directory")

    elif "program files" in path:
        reasons.append("Installed application")

    else:
        score += 15
        reasons.append("Unknown executable location")

    if cpu > 50:
        score += 20
        reasons.append("High CPU usage")

    if ram > 10:
        score += 20
        reasons.append("High RAM usage")

    if score >= 70:
        level = "HIGH"
    elif score >= 30:
        level = "MEDIUM"
    else:
        level = "LOW"

    return score, level, reasons