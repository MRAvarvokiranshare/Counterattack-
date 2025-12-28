from engine import DetectionEngine

engine = DetectionEngine()

print("Anti-DDoS Engine CLI Test")
print("Type IP address or 'exit'\n")

while True:
    ip = input("IP> ").strip()
    if ip.lower() == "exit":
        break

    result = engine.inspect_ip(ip)
    print("Result:", result)
    print("Metrics:", engine.get_metrics())
    print("-" * 40)
