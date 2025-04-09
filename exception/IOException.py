class IOException(Exception):
    def __init__(self, message="File I/O error occurred."):
        super().__init__(message)
