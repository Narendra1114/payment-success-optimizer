from fastapi import FastAPI
from app.api.predict import router as predict_router

app = FastAPI(title="Payment Success Optimizer")

app.include_router(predict_router)

@app.get("/")
def home():
    return {"message": "API is running"}