
waste = {
    "Plastic": 45,
    "Organic": 80,
    "Electronic": 18,
    "Construction": 65
}

total = sum(waste.values())

for category, amount in waste.items():
    status = "High" if amount >= 60 else "Normal"
    print(category, "-", amount, "kg -", status)

print("Total Waste:", total, "kg")
print("Largest Category:", max(waste, key=waste.get))
