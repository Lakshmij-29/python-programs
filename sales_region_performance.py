
regions = {
    "South": 850000,
    "North": 720000,
    "East": 640000,
    "West": 910000
}

total = sum(regions.values())
average = total / len(regions)

for region, revenue in regions.items():
    print(region, "- Revenue:", revenue)

print("Total Revenue:", total)
print("Average Revenue:", round(average, 2))
print("Top Region:", max(regions, key=regions.get))
