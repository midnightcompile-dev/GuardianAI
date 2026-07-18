import time

from collectors.process_collector import get_running_processes
from history.process_history import (
    get_previous_processes,
    update_processes,
)

print("GuardianAI Live Process Monitor")
print("=" * 60)

while True:
    processes = get_running_processes()

    process_names = []

    for process in processes:
        if process["name"]:
            process_names.append(process["name"])

    current_processes = set(process_names)
    previous_processes = get_previous_processes()

    new_processes = current_processes - previous_processes

    if new_processes:
        print("\n🆕 New Process Detected:")
        for process in sorted(new_processes):
            print(f"   • {process}")

    update_processes(process_names)

    time.sleep(3)