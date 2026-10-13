
response_times = [120, 240, 180, 850, 320, 1100]

average = sum(response_times) / len(response_times)
slow = sum(time > 500 for time in response_times)

print("Average Response:", round(average, 2), "ms")
print("Fastest Response:", min(response_times), "ms")
print("Slowest Response:", max(response_times), "ms")
print("Slow Requests:", slow)

if average > 500:
    print("Performance Alert")
else:
    print("Performance Acceptable")
