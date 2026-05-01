def build_features(data):
    return [
        data.amount,
        data.payment_method,
        data.bank,
        data.hour,
        data.user_success_rate,
    ]