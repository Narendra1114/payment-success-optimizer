import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "amount": 1200,
    "payment_method": 1,
    "bank": 2,
    "hour": 14,
    "user_success_rate": 0.75
}

response = requests.post(url, json=data)
print(response.json())