import numpy as np
import matplotlib.pyplot as plt

width = 800
height = 800

image = np.zeros((height, width))

for x in range(width):
    for y in range(height):

        c = complex(
            (x-width/2)*4/width,
            (y-height/2)*4/height
        )

        z = 0
        iteration = 0

        while abs(z) <= 2 and iteration < 50:
            z = z*z + c
            iteration += 1

        image[y, x] = iteration

plt.imshow(image)

plt.title("Mandelbrot Fractal")
plt.show()
