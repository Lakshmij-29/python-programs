
parking_slots = {
    "Zone_A": 45,
    "Zone_B": 38,
    "Zone_C": 50,
    "Zone_D": 29
}

capacity = 60

for zone, occupied in parking_slots.items():
    available = capacity - occupied
    print(zone, "- Available:", available)

total_occupied = sum(parking_slots.values())
print("Total Occupied:", total_occupied)
print("Total Available:", len(parking_slots) * capacity - total_occupied)
