

employees = {
    "Aman": [90, 85, 88],
    "Riya": [95, 92, 96],
    "Kiran": [72, 78, 75],
    "Neha": [88, 91, 84]
}

for name, scores in employees.items():
    average = sum(scores) / len(scores)
    print(name, "-", round(average, 2))

best = max(employees, key=lambda x: sum(employees[x]) / 3)
print("Top Performer:", best)
