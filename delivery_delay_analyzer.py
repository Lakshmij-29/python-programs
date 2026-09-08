deliveries = {
    "Package_101": 0,
    "Package_102": 2,
    "Package_103": 5,
    "Package_104": 1
}

delayed = 0

for package, days in deliveries.items():
    if days > 0:
        delayed += 1
        print(package, "Delayed by", days, "days")
    else:
        print(package, "On Time")

print("Total Delayed Packages:", delayed)
