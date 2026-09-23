models = {
    "Model_A": [0.91, 0.89, 0.93],
    "Model_B": [0.86, 0.88, 0.84],
    "Model_C": [0.94, 0.92, 0.95]
}

for model, scores in models.items():
    average = sum(scores) / len(scores)
    print(model, "-", round(average * 100, 2), "%")

best = max(models, key=lambda x: sum(models[x]) / len(models[x]))
print("Highest Average Accuracy:", best)
