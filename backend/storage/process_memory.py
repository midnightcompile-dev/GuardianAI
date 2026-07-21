import json
import os

MEMORY_FILE = os.path.join(
    os.path.dirname(__file__),
    "known_processes.json"
)


def load_known_processes():
    try:
        with open(MEMORY_FILE, "r") as file:
            return set(json.load(file))
    except:
        return set()


def save_known_processes(processes):
    with open(MEMORY_FILE, "w") as file:
        json.dump(sorted(list(processes)), file, indent=4)