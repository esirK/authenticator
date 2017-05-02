class AuthException(Exception):
    def __init__(self, username, user=None):
        """ 
        Create an AuthException taking in  a username and
        an optional user. if only username is specified then only password
         length will only be checked
         """
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExists(AuthException):
    pass


class PasswordTooShort(AuthException):
    pass


class InvalidUsername(AuthException):
    pass


class InvalidPassword(AuthException):
    pass


class PermissionError(Exception):
    pass


class NotLoggedInError(AuthException):
    pass


class NotPermittedError(AuthException):
    pass
