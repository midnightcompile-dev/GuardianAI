from collectors.process_collector import get_running_processes
from storage.process_memory import (
    load_known_processes,
    save_known_processes,
)

known = load_known_processes()

processes = get_running_processes()

current = set()

print("GuardianAI Learning")
print("=" * 60)

for process in processes:

    name = process["name"]

    if not name:
        continue

    current.add(name)

    if name not in known:
        print(f"🆕 Learned: {name}")

known.update(current)

save_known_processes(known)

print("\nLearning Complete!")