# decision_boundary.py

from sklearn.datasets import make_moons
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import numpy as np

# Generate dataset
X, y = make_moons(n_samples=500, noise=0.2)

# Train model
model = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=500)
model.fit(X, y)

# Create mesh
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

xx, yy = np.meshgrid(
    np.arange(x_min, x_max, 0.01),
    np.arange(y_min, y_max, 0.01)
)

Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Plot
plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.5)

plt.scatter(X[:, 0], X[:, 1], c=y)

plt.title("Neural Network Decision Boundary")
plt.show()
