import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("train_dataset.csv")
df.head()

X = df.drop(columns=["smoking"])
y = df["smoking"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


def evaluate_model(model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy, y_pred


model = KNeighborsClassifier(n_neighbors=5)  # classifies by 5 nearest points
accuracy, y_pred = evaluate_model(model, X_train, y_train, X_test, y_test)

print(f"KNN Accuracy {accuracy * 100:.2f}%")
