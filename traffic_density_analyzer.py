vehicles = [42, 58, 76, 91, 63, 48]
average = sum(vehicles) / len(vehicles)

print("Average Vehicles:", round(average, 2))
print("Peak Traffic:", max(vehicles))

for count in vehicles:
    if count > 75:
        print(count, "- High Traffic")
    else:
        print(count, "- Normal Traffic")
