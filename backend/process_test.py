from collectors.process_collector import get_running_processes
from analyzer.process_analyzer import analyze_process

processes = get_running_processes()

print("GuardianAI Process Analysis")
print("=" * 80)

for process in processes[:20]:
    status = analyze_process(process)

    print(f"Name   : {process['name']}")
    print(f"Status : {status}")
    print(f"Path   : {process['exe']}")
    print("-" * 80)