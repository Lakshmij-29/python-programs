import matplotlib.pyplot as plt

n = [10, 50, 100, 500]
bubble = [n_i**2 for n_i in n]
linear = n

plt.plot(n, bubble, label="O(n^2)")
plt.plot(n, linear, label="O(n)")
plt.legend()
plt.title("Time Complexity Comparison")
plt.show()
