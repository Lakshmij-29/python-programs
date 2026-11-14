
from sklearn.model_selection import train_test_split

features = [[20], [25], [30], [35], [40], [45], [50], [55]]
labels = [0, 0, 0, 1, 1, 1, 1, 1]

x_train, x_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.25, random_state=42
)

print("Training Records:", len(x_train))
print("Testing Records:", len(x_test))
print("Training Labels:", y_train)
print("Testing Labels:", y_test)
