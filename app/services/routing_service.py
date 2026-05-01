def choose_gateway(success_prob):
    if success_prob > 0.8:
        return "Primary Gateway"
    elif success_prob > 0.5:
        return "Secondary Gateway"
    else:
        return "Retry with UPI"