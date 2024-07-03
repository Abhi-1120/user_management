__all__ = ['errors']

errors = {
    "Exception": {
        'ok': False,
        'error': 'INTERNAL_SERVER_ERROR',
        'message': "Oops! Something went wrong. Please try again later.",
        'status': 500},
    'InternalServerException': {
        'ok': False,
        'error': 'SERVER_ERROR',
        'message': "Service is down. Please try again after some time!",
        'status': 500},
    "UserAlreadyExistException": {
        'ok': False,
        'error': 'USER_ALREADY_EXIST',
        'message': "Oops! A user with the same username or email already exists in the system.",
        'status': 400
    },
    "UserNotExistException": {
        'ok': False,
        'error': 'USER_NOT_EXIST',
        'message': "User Not Found",
        'status': 404
    }
}
