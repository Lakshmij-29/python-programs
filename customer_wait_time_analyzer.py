wait_times = [8, 12, 15, 7, 21, 18, 10]

average = sum(wait_times) / len(wait_times)
long_waits = [time for time in wait_times if time > 15]

print("Average Wait:", round(average, 2), "minutes")
print("Long Wait Cases:", len(long_waits))
print("Longest Wait:", max(wait_times), "minutes")

if average > 15:
    print("Service improvement required")
