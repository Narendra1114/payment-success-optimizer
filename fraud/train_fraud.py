import pandas as pd
from xgboost import XGBClassifier
import pickle
import os

os.makedirs("fraud", exist_ok=True)

df = pd.read_csv("data/fraud_data.csv")

X = df.drop("is_fraud", axis=1)
y = df["is_fraud"]

model = XGBClassifier(eval_metric='logloss')
model.fit(X, y)

with open("fraud/fraud_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Fraud model trained!")