class UserException(Exception):
    pass


class Error(UserException):
    def __init__(self, message):
        self.message = message
        return message
