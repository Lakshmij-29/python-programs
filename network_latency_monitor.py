latency = [42, 55, 38, 91, 47, 120]

average = sum(latency) / len(latency)
slow_requests = [x for x in latency if x > 80]

print("Average Latency:", round(average, 2), "ms")
print("Slow Requests:", len(slow_requests))

if average > 70:
    print("Network performance needs attention")
