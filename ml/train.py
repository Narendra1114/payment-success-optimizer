import pandas as pd
from xgboost import XGBClassifier
import pickle

df = pd.read_csv("data/transactions.csv")

X = df.drop("success", axis=1)
y = df["success"]

model = XGBClassifier(eval_metric='logloss')
model.fit(X, y)

with open("app/models/xgb_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")