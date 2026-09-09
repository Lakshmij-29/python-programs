departments = {
    "Emergency": 92,
    "Cardiology": 74,
    "Neurology": 61,
    "Pediatrics": 83
}

for department, load in departments.items():
    status = "Critical" if load > 85 else "High" if load > 70 else "Normal"
    print(department, "-", load, "% -", status)

highest = max(departments, key=departments.get)
print("Highest Load:", highest)
