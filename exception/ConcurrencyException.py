class ConcurrencyException(Exception):
    def __init__(self, message="Data conflict detected. Please try again."):
        super().__init__(message)
