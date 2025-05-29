# 🚀 MLOps: Tự động cập nhật model với MLflow & AI Agent

Dự án này là ví dụ thực hành cho **Buổi 9 - MLOps CI/CD**. Pipeline CI/CD sử dụng **MLflow để log model**, kết hợp với **AI Agent để chọn mô hình tốt nhất** và **tự động cập nhật vào MLflow Registry**.

---

## 🎯 Mục tiêu

* Tự động huấn luyện mô hình mới khi có code cập nhật.
* So sánh mô hình mới với mô hình cũ trong MLflow Registry.
* Nếu tốt hơn → cập nhật model vào Production.
* Nếu pipeline lỗi → gửi thông báo qua Zapier (Slack/Email).

---

## 📁 Cấu trúc thư mục

```
mlops-ai-agent-pipeline/
├── agents/
│   └── model_selector_agent.py         # Agent chọn model tốt nhất
├── scripts/
│   └── train_model.py                  # Train + log model
├── models/
│   └── model_latest.pkl                # Model mới
├── .github/workflows/
│   └── ci-cd-mlflow.yaml               # GitHub Actions workflow
├── requirements.txt
├── README.md
```

---

## 📦 Cài đặt

```bash
pip install -r requirements.txt
```

---

## 🚀 Chạy pipeline local (không cần CI/CD)

```bash
python scripts/train_model.py
python agents/model_selector_agent.py
```

---

## ⚙️ Cấu hình MLflow Tracking Server

Bạn cần chạy MLflow UI local hoặc dùng server cloud:

```bash
mlflow ui --port 5000
```

Rồi sửa URI trong `model_selector_agent.py`:

```python
mlflow.set_tracking_uri("http://localhost:5000")
```

---

## 🧪 CI/CD với GitHub Actions

Tự động chạy khi bạn push code thay đổi.

* Huấn luyện model mới
* Agent chọn model tốt hơn
* Tự động cập nhật model Production
* Gửi thông báo nếu lỗi

---

## 🧠 AI Agent hoạt động thế nào?

1. Đọc model mới từ file `model_latest.pkl`
2. Lấy model tốt nhất trong Registry (stage=Production)
3. So sánh accuracy
4. Nếu tốt hơn → đăng ký lại model mới vào Registry

---

## 📬 Thông báo Zapier

Tùy chọn: bạn có thể dùng Zapier webhook để gửi lỗi pipeline tới email hoặc Slack:

```yaml
curl -X POST https://hooks.zapier.com/hooks/catch/your_zap_id \
  -H "Content-Type: application/json" \
  -d '{"message": "Pipeline failed"}'
```

## 📚 Tham khảo

* [MLflow Tracking & Registry](https://mlflow.org/docs/latest/tracking.html)
* [GitHub Actions](https://docs.github.com/en/actions)
* [Zapier Webhook Setup](https://zapier.com/help/create/code-webhooks/send-webhooks-in-zapier)
