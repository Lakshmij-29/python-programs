appointments = {
    "Dr_Smith": 4,
    "Dr_John": 8,
    "Dr_Riya": 2
}

for doctor, slots in appointments.items():
    print(doctor, "- Available Slots:", slots)

    if slots < 3:
        print("Almost fully booked")

print("Schedule updated")
