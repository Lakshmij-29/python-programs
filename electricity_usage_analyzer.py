usage = [420, 390, 510, 480, 450]

total = sum(usage)
average = total / len(usage)
peak = max(usage)

print("Total Usage:", total, "kWh")
print("Average Usage:", round(average, 2), "kWh")
print("Peak Usage:", peak, "kWh")

if peak > 500:
    print("High consumption detected")
