
bookings = {
    "Flight_A": 145,
    "Flight_B": 172,
    "Flight_C": 128,
    "Flight_D": 189
}

capacity = 200

for flight, booked in bookings.items():
    occupancy = booked / capacity * 100
    print(flight, "-", round(occupancy, 2), "%")

print("Most Booked:", max(bookings, key=bookings.get))
