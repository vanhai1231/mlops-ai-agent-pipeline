import os
import pickle
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Tải dữ liệu
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Huấn luyện mô hình
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)

# Thiết lập thư mục lưu model
os.makedirs("models", exist_ok=True)

# Bắt đầu run trong MLflow
with mlflow.start_run() as run:
    print(f"Run ID: {run.info.run_id}")

    # Log metrics và model
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "model")

    # Lưu model ra file để AI Agent sử dụng
    model_path = "models/model_latest.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print(f"Accuracy logged: {accuracy:.4f}")
    print(f"Model saved to {model_path}")
