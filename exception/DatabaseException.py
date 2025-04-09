class DatabaseException(Exception):
    def __init__(self, message="Database error occurred."):
        super().__init__(message)
