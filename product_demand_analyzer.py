sales = {
    "Laptop": 120,
    "Phone": 280,
    "Tablet": 160,
    "Headphones": 340
}

for product, quantity in sales.items():
    demand = "High" if quantity >= 250 else "Medium" if quantity >= 150 else "Low"
    print(product, "-", quantity, "units -", demand)

top_product = max(sales, key=sales.get)
print("Highest Demand:", top_product)
