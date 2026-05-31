total_slots = 50
occupied = int(input("Occupied slots: "))

available = total_slots - occupied

print("Available slots:", available)

if available < 10:
    print("Parking almost full")
else:
    print("Parking available")
