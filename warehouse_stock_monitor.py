stock = {
    "Mouse": 12,
    "Keyboard": 4,
    "Monitor": 20
}

for item, qty in stock.items():
    print(item, "- Stock:", qty)

    if qty < 5:
        print("Reorder required")

print("Warehouse check completed")
