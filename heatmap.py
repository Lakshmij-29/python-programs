import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.random.seed(0)
data=np.random.rand(10,10)
plt.imshow(data,cmap="viridis",interpolation="nearest")
plt.colorbar()
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("heatmap")
plt.show()
