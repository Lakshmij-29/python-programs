customers = {
    "Aman": 2,
    "Riya": 14,
    "John": 30
}

for name, inactive_days in customers.items():
    if inactive_days > 20:
        print(name, "- High churn risk")
    elif inactive_days > 7:
        print(name, "- Medium churn risk")
    else:
        print(name, "- Active customer")
