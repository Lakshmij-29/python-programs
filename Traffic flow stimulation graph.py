import random
import matplotlib.pyplot as plt

traffic = [random.randint(10, 100) for _ in range(10)]

plt.plot(traffic, marker='o')
plt.title("Traffic Flow Over Time")
plt.xlabel("Time")
plt.ylabel("Number of Cars")
plt.show()
