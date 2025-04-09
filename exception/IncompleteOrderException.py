class IncompleteOrderException(Exception):
    def __init__(self, message="Order details are incomplete."):
        super().__init__(message)