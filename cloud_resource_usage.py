
resources = {
    "CPU": 78,
    "Memory": 65,
    "Storage": 91,
    "Bandwidth": 54
}

for resource, usage in resources.items():
    status = "Critical" if usage >= 90 else "Normal"
    print(resource, "-", usage, "% -", status)

average = sum(resources.values()) / len(resources)
print("Average Utilization:", round(average, 2), "%")
