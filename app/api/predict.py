from fastapi import APIRouter
from app.services.feature_engineering import build_features
from app.services.model_service import ModelService
from app.services.routing_service import choose_gateway
from app.schemas.request_schema import PaymentRequest

from fraud.fraud_service import FraudService  # if using fraud

# ✅ DEFINE ROUTER FIRST
router = APIRouter()

# Load models
model = ModelService()
fraud_model = FraudService()

@router.post("/predict")
def predict(data: PaymentRequest):
    features = build_features(data)
    prob = model.predict(features)

    fraud_features = [
        data.amount,
        5,
        0.3,
        0
    ]

    fraud_prob = fraud_model.predict(fraud_features)

    route = choose_gateway(prob)

    return {
        "success_probability": prob,
        "fraud_probability": fraud_prob,
        "recommended_route": route
    }