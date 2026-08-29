usage = {
    "Monday": 420,
    "Tuesday": 390,
    "Wednesday": 510,
    "Thursday": 450
}

total = sum(usage.values())
average = total / len(usage)

print("Total Usage:", total, "Litres")
print("Daily Average:", round(average, 2), "Litres")
print("Highest Usage:", max(usage.values()), "Litres")
