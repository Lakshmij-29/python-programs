traffic = {
    "Monday": 4200,
    "Tuesday": 5100,
    "Wednesday": 4800,
    "Thursday": 6200,
    "Friday": 7100
}

total = sum(traffic.values())
average = total / len(traffic)
peak_day = max(traffic, key=traffic.get)

print("Total Visitors:", total)
print("Average Visitors:", round(average))
print("Peak Traffic Day:", peak_day)
