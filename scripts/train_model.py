import mlflow
import mlflow.sklearn
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load dữ liệu mẫu
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train mô hình
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)

# Bắt đầu log vào MLflow
with mlflow.start_run() as run:
    print(f"Run ID: {run.info.run_id}")
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "model")

    # Lưu model ra file để agent so sánh
    with open("models/model_latest.pkl", "wb") as f:
        pickle.dump(model, f)

    print(f"Logged accuracy: {accuracy}")
