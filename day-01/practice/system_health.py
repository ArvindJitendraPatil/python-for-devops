# system_health.py
import psutil

print("Choose option:")
print("1. CPU Usage")
print("2. Memory Usage")
print("3. Disk Usage")
print("4. Network Usage")

choice = input("Enter choice (1-4): ")

if choice == "1":
    print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
elif choice == "2":
    print("Memory Usage:", psutil.virtual_memory().percent, "%")
elif choice == "3":
    print("Disk Usage:", psutil.disk_usage('/').percent, "%")
elif choice == "4":
    net = psutil.net_io_counters()
    print("Bytes Sent:", net.bytes_sent)
    print("Bytes Received:", net.bytes_recv)
else:
    print("Invalid choice!")
