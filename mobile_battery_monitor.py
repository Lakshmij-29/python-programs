battery_levels = {
    "Phone_A": 82,
    "Phone_B": 19,
    "Phone_C": 47,
    "Phone_D": 8
}

for device, battery in battery_levels.items():
    if battery <= 20:
        status = "Critical"
    elif battery <= 50:
        status = "Low"
    else:
        status = "Healthy"

    print(device, "-", battery, "% -", status)
