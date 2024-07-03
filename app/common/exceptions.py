from builtins import Exception

__all__ = ["GeneralException", "UserAlreadyExistException", "UserNotExistException"]


class GeneralException(Exception):
    pass


class UserAlreadyExistException(GeneralException):
    pass


class UserNotExistException(GeneralException):
    pass
