from collectors.process_collector import get_running_processes
from collectors.signature_collector import get_company_name

processes = get_running_processes()

print("GuardianAI Publisher Scan")
print("=" * 80)

for process in processes[:20]:

    company = get_company_name(process["exe"])

    print(f"Process   : {process['name']}")
    print(f"Company   : {company}")
    print(f"Path      : {process['exe']}")
    print("-" * 80)