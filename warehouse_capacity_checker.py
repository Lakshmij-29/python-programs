capacity = 1000
current_stock = int(input("Current stock units: "))

usage = current_stock / capacity * 100

print("Warehouse Usage:", round(usage, 2), "%")

if usage > 90:
    print("Capacity Critical")
else:
    print("Capacity Normal")
