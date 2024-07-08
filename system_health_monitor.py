import psutil

# Define thresholds (example thresholds, adjust as needed)
CPU_THRESHOLD = 80.0  # percentage
MEMORY_THRESHOLD = 90.0  # percentage
DISK_THRESHOLD = 85.0   # percentage

def check_system_health():
    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > CPU_THRESHOLD:
        print(f"Alert: CPU Usage is above {CPU_THRESHOLD}%")

    # Memory usage
    memory_usage = psutil.virtual_memory().percent
    print(f"Memory Usage: {memory_usage}%")
    if memory_usage > MEMORY_THRESHOLD:
        print(f"Alert: Memory Usage is above {MEMORY_THRESHOLD}%")

    # Disk usage
    disk_usage = psutil.disk_usage('/').percent
    print(f"Disk Usage: {disk_usage}%")
    if disk_usage > DISK_THRESHOLD:
        print(f"Alert: Disk Usage is above {DISK_THRESHOLD}%")

    # Running processes
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        print(f"Process: {proc.info}")

if __name__ == "__main__":
    check_system_health()