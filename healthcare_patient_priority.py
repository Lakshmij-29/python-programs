age = int(input("Patient age: "))
severity = int(input("Severity score (1-10): "))

if severity >= 8 or age > 65:
    priority = "High"
elif severity >= 5:
    priority = "Medium"
else:
    priority = "Low"

print("Treatment Priority:", priority)
