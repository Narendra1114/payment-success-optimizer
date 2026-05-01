import streamlit as st
import requests

st.title("💳 AI Payment + Fraud Intelligence Dashboard")

st.sidebar.header("Input Transaction")

amount = st.sidebar.slider("Amount", 100, 10000, 1000)
payment_method = st.sidebar.selectbox("Method", [0,1,2])
bank = st.sidebar.selectbox("Bank", [0,1,2,3,4])
hour = st.sidebar.slider("Hour", 0, 23, 12)
user_success_rate = st.sidebar.slider("User Success Rate", 0.0, 1.0, 0.7)

if st.sidebar.button("Analyze Transaction"):

    data = {
        "amount": amount,
        "payment_method": payment_method,
        "bank": bank,
        "hour": hour,
        "user_success_rate": user_success_rate
    }

    res = requests.post("http://127.0.0.1:8000/predict", json=data)

    if res.status_code == 200:
        result = res.json()

        st.subheader("📈 Results")

        st.metric("Success Probability", f"{result['success_probability']:.2f}")
        st.metric("Fraud Probability", f"{result['fraud_probability']:.2f}")

        st.success(f"Recommended Route: {result['recommended_route']}")

        if result['fraud_probability'] > 0.7:
            st.error("⚠️ High Fraud Risk!")
    else:
        st.error("API not running!")