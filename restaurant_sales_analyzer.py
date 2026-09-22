sales = {
    "Pizza": 145,
    "Burger": 210,
    "Pasta": 120,
    "Sandwich": 175
}

total = sum(sales.values())
average = total / len(sales)
best_seller = max(sales, key=sales.get)

print("Total Items Sold:", total)
print("Average Sales:", round(average, 2))
print("Best Seller:", best_seller)

for item, count in sales.items():
    print(item, "-", count)
