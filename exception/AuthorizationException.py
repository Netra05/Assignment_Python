class AuthorizationException(Exception):
    def __init__(self, message="You are not authorized to access this resource."):
        super().__init__(message)
