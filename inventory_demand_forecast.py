
stock = {"Laptop": 15, "Mouse": 8, "Keyboard": 12}
weekly_sales = {"Laptop": 5, "Mouse": 6, "Keyboard": 4}

for item, quantity in stock.items():
    demand = weekly_sales[item]
    remaining = quantity - demand
    print(item, "- Remaining:", remaining)

    if remaining < demand:
        print("Restock Recommended:", item)
