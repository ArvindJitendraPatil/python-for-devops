#This task builds the foundation for **automation, monitoring, and reliability**.
import psutil
import os
# To check cpu usage

cpu_limit = float(input("Enter the limit % :"))  # threshold in percent
print(f"{cpu_limit}%") 

current_cpu_usage = psutil.cpu_percent(interval=1)
print(f"{current_cpu_usage}%")
if current_cpu_usage > cpu_limit:
    print("CPU usage is HIGHER than your limit")
else:
    print("CPU usage is within limit")

# To check memory usage 
memory_limit = float(input("Enter the limit % :")) # threshold in percent
print(f"{memory_limit}%")

memory_usage = psutil.virtual_memory().percent
print(f"{memory_usage}%")

if memory_usage > memory_limit:
    print("Memory usage is HIGHER than your limit % :")
else:
    print("Memory usage is within limit")

# To check disk usage
# Pick the path to monitor:
# Windows -> "C:\\" 
# Linux/Mac -> "/"

disk_path = "C:\\" if os.name == "nt" else "/"

disk_limit = float(input("Enter the limit % :"))  # threshold in percent
print(f"{disk_limit}%")

disk_usage = psutil.disk_usage(disk_path).percent
print(f"{disk_usage}%")

if disk_usage > disk_limit:
    print("Disk usage is HIGHER than your limit")
else:
    print("Disk usage is within limit")
