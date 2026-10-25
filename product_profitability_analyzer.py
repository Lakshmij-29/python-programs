
products = {
    "Laptop": [45000, 55000, 12],
    "Phone": [15000, 19000, 30],
    "Tablet": [12000, 14500, 18]
}

total_profit = 0

for name, values in products.items():
    cost, price, quantity = values
    profit = (price - cost) * quantity
    total_profit += profit
    print(name, "Profit:", profit)

print("Total Profit:", total_profit)
