
openings = {
    "Python Developer": 120,
    "Data Analyst": 95,
    "AI Engineer": 150,
    "Web Developer": 110
}

total = sum(openings.values())
average = total / len(openings)

print("Total Openings:", total)
print("Average Openings:", round(average, 2))
print("Most In-Demand:", max(openings, key=openings.get))

for role, count in openings.items():
    print(role, "-", count)
