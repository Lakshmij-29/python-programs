temperatures = [68, 72, 75, 91, 78, 94]

average = sum(temperatures) / len(temperatures)
alerts = [temp for temp in temperatures if temp > 85]

print("Average Temperature:", round(average, 2))
print("Temperature Alerts:", len(alerts))
print("Maximum Temperature:", max(temperatures))

if alerts:
    print("Machine Inspection Required")
