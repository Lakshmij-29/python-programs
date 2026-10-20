
customers = {
    "Aman": 12000,
    "Riya": 4500,
    "Neha": 18000,
    "Kiran": 2000
}

for name, spending in customers.items():
    if spending >= 10000:
        segment = "Premium"
    elif spending >= 4000:
        segment = "Regular"
    else:
        segment = "Budget"

    print(name, "-", segment, "-", spending)
