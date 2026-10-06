
water_usage = {
    "Kitchen": 85,
    "Bathroom": 120,
    "Garden": 160,
    "Laundry": 95
}

total = sum(water_usage.values())
highest = max(water_usage, key=water_usage.get)

print("Total Usage:", total, "Litres")
print("Highest Usage:", highest)

for area, usage in water_usage.items():
    print(area, "-", usage, "Litres")
