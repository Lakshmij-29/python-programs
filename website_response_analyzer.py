times = [120, 150, 90, 300, 110]

average = sum(times) / len(times)

print("Average Response Time:", average, "ms")

slow = [t for t in times if t > 200]

print("Slow Requests:", len(slow))

if slow:
    print("Performance optimization needed")
