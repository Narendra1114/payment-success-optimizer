import pandas as pd
import numpy as np

np.random.seed(42)

n = 5000

df = pd.DataFrame({
    "amount": np.random.randint(100, 10000, n),
    "transaction_velocity": np.random.randint(1, 20, n),
    "device_risk": np.random.uniform(0, 1, n),
    "location_mismatch": np.random.randint(0, 2, n),
})

# fraud logic
df["is_fraud"] = (
    (df["amount"] > 7000) |
    (df["transaction_velocity"] > 15) |
    (df["device_risk"] > 0.8)
).astype(int)

df.to_csv("data/fraud_data.csv", index=False)
print("Fraud data generated!")