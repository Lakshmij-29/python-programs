customers = {
    "Aman": 2,
    "Riya": 8,
    "Kiran": 5,
    "Neha": 10
}

for name, inactive_days in customers.items():
    if inactive_days >= 8:
        risk = "High"
    elif inactive_days >= 5:
        risk = "Medium"
    else:
        risk = "Low"

    print(name, "-", risk)
