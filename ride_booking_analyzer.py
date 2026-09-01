rides = {
    "Monday": 120,
    "Tuesday": 145,
    "Wednesday": 132,
    "Thursday": 178
}

total = sum(rides.values())
average = total / len(rides)
peak_day = max(rides, key=rides.get)

print("Total Rides:", total)
print("Average Daily Rides:", round(average, 2))
print("Peak Day:", peak_day)
