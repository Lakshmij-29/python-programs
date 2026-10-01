
rides = {
    "Ride_101": 180,
    "Ride_102": 250,
    "Ride_103": 145,
    "Ride_104": 320
}

total = sum(rides.values())
average = total / len(rides)

print("Total Fare:", total)
print("Average Fare:", round(average, 2))

highest = max(rides, key=rides.get)
print("Highest Fare Ride:", highest)
