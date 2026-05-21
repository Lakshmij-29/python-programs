usage = [2.5, 3.1, 5.2, 7.8, 4.0]

average = sum(usage) / len(usage)

print("Average Usage:", round(average, 2), "GB")

peak = max(usage)
print("Peak Usage:", peak, "GB")

if peak > 7:
    print("High network traffic detected")
