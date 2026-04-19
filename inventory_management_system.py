items = {"Pen": 20, "Book": 15, "Bag": 5}

product = input("Enter product name: ")
qty = int(input("Enter quantity sold: "))

if product in items and items[product] >= qty:
    items[product] -= qty
    print("Sale completed ")
else:
    print("Not enough stock ")

print("Updated Inventory:", items)
