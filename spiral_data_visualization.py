import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 10*np.pi, 1000)

r = theta

x = r*np.cos(theta)
y = r*np.sin(theta)

plt.plot(x, y)

plt.title("Spiral Data Pattern")
plt.axis("equal")
plt.show()
