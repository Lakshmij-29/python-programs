
orders = {
    "Zone_A": 145,
    "Zone_B": 210,
    "Zone_C": 175,
    "Zone_D": 95
}

total = sum(orders.values())
highest_zone = max(orders, key=orders.get)

print("Total Orders:", total)
print("Highest Order Zone:", highest_zone)

for zone, count in orders.items():
    print(zone, "-", count)
