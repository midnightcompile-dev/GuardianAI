from collectors.process_collector import get_running_processes
from analyzer.risk_analyzer import calculate_risk

processes = get_running_processes()

print("GuardianAI Security Scan")
print("=" * 80)

found = False

for process in processes:

    score, level, reasons = calculate_risk(process)

    if score >= 30:

        found = True

        print(f"Name       : {process['name']}")
        print(f"Risk Score : {score}/100")
        print(f"Risk Level : {level}")

        print("Reasons:")
        for reason in reasons:
            print(f"  • {reason}")

        print(f"Path : {process['exe']}")
        print("-" * 80)

if not found:
    print("✅ No suspicious processes were found.")