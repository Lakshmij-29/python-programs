cpu = int(input("CPU usage %: "))
memory = int(input("Memory usage %: "))

if cpu > 85 or memory > 85:
    status = "Critical"
elif cpu > 60 or memory > 60:
    status = "Warning"
else:
    status = "Healthy"

print("Server Status:", status)
