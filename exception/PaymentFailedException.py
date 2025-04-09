class PaymentFailedException(Exception):
    def __init__(self, message="Payment failed. Please try again."):
        super().__init__(message)
