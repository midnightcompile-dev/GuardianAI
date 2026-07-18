import psutil


def get_system_info():
    gb = 1024 ** 3

    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    battery = psutil.sensors_battery()

    return {
        "cpu": cpu_usage,
        "memory": memory,
        "disk": disk,
        "battery": battery,
        "gb": gb,
    }