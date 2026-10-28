import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
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


model = LogisticRegression(random_state=42, max_iter=1000)
accuracy, y_pred = evaluate_model(model, X_train, y_train, X_test, y_test)

print(f"Logistic Regression Accuracy {accuracy * 100:.2f}%")
