class BaseException(Exception):
    message: str = "Internal Server Error"
    
    def __init__(self, message: str | None = None) -> None:

        if message:
            self.message = message


class NotFounException(BaseException):
    message = "Not Found"