import psutil


def get_running_processes():
    processes = []

    for process in psutil.process_iter([
        "pid",
        "name",
        "cpu_percent",
        "memory_percent",
        "exe",
    ]):
        try:
            processes.append(process.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    return processes