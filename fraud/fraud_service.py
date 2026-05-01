import pickle

class FraudService:
    def __init__(self):
        with open("fraud/fraud_model.pkl", "rb") as f:
            self.model = pickle.load(f)

    def predict(self, features):
        prob = self.model.predict_proba([features])[0][1]
        return float(prob)