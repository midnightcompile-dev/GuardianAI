def analyze_process(process):
    path = process["exe"]

    if path is None or path == "":
        return "⚪ System Process"

    path = path.lower()

    if "windows" in path:
        return "✅ Trusted Windows Process"

    if "program files" in path:
        return "✅ Installed Application"

    if "temp" in path:
        return "⚠️ Running from Temp Folder"

    if "downloads" in path:
        return "⚠️ Running from Downloads Folder"

    return "❓ Unknown Location"