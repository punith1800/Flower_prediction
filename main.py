
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.20, stratify=iris.target, random_state=42
)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Species:", ", ".join(iris.target_names))
print(f"Training: {len(X_train)} | Testing: {len(X_test)}")
print(f"Accuracy: {accuracy_score(y_test, predictions):.2%}")
print("Confusion matrix:\n", confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions, target_names=iris.target_names))

sample = [[6.5, 3.0, 5.8, 2.2]]
print("Sample prediction:", iris.target_names[model.predict(sample)[0]])
