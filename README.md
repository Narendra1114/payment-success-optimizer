# 💳 AI Payment Success Optimizer + Fraud Detection System

## 🚀 Overview
This project simulates a real-world fintech system inspired by Razorpay.

It combines:
- Payment success prediction (ML)
- Fraud detection system
- Kafka-based real-time streaming
- Streamlit dashboard

---

## 🧠 Architecture

Client → API → Kafka → Consumer → ML Models → Decision Engine → Dashboard

---

## 🔥 Features

- Predict payment success probability
- Detect fraudulent transactions
- Smart routing system
- Real-time event streaming (Kafka)
- Interactive dashboard

---

## 🛠️ Tech Stack

- FastAPI
- XGBoost
- Kafka
- Streamlit
- Docker (optional)

---

## ▶️ How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Generate data
python data/generate_data.py  
python data/generate_fraud_data.py  

### 3. Train models
python ml/train.py  
python fraud/train_fraud.py  

### 4. Start Kafka (Docker)

### 5. Run consumer
python kafka/consumer.py  

### 6. Start API
uvicorn app.main:app --reload  

### 7. Run dashboard
streamlit run dashboard/app.py  

---

## 📊 Sample Output

- Success Probability: 0.82  
- Fraud Probability: 0.15  
- Recommended Route: Primary Gateway  

---

## 🎯 Business Impact

- Improves payment success rate  
- Reduces fraud risk  
- Enables real-time decision making  

---
