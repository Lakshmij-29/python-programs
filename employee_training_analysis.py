
training = {
    "Aman": 85,
    "Riya": 92,
    "John": 68,
    "Neha": 96
}

average = sum(training.values()) / len(training)

for employee, score in training.items():
    status = "Completed" if score >= 75 else "Needs Training"
    print(employee, "-", score, "-", status)

print("Average Score:", round(average, 2))
