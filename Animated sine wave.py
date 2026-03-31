import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
line, = ax.plot(x, y)

def animate(i):
    line.set_ydata(np.sin(x + i/10))
    return line,

ani = FuncAnimation(fig, animate, frames=100, interval=50)
plt.show()
