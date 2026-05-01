from pydantic import BaseModel

class PaymentRequest(BaseModel):
    amount: float
    payment_method: int
    bank: int
    hour: int
    user_success_rate: float