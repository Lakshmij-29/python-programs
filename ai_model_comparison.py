
models = {
    "Random Forest": 91.5,
    "Decision Tree": 86.2,
    "Logistic Regression": 88.7,
    "SVM": 90.1
}

for model, accuracy in models.items():
    print(model, "-", accuracy, "%")

best_model = max(models, key=models.get)

print("Best Model:", best_model)
print("Best Accuracy:", models[best_model], "%")
