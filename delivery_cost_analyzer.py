
deliveries = {
    "Package_A": 120,
    "Package_B": 250,
    "Package_C": 180,
    "Package_D": 320
}

total = sum(deliveries.values())
average = total / len(deliveries)

print("Total Delivery Cost:", total)
print("Average Cost:", round(average, 2))
print("Most Expensive:", max(deliveries, key=deliveries.get))
