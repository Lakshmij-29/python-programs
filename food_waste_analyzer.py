waste = {
    "Monday": 12,
    "Tuesday": 18,
    "Wednesday": 9,
    "Thursday": 22
}

total = sum(waste.values())
average = total / len(waste)

print("Total Waste:", total, "kg")
print("Average Waste:", round(average, 2), "kg")

if average > 15:
    print("Food waste is above target")
