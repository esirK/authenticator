from src.AuthException import UsernameAlreadyExists, PasswordTooShort, InvalidUsername, InvalidPassword
from src.User import User


class Authenticator:
    def __init__(self):
        """
        Construct an authenticator to manage users login and log out
        """
        self.users = {}

    def add_user(self, username, password):
        """
        :param password: checks the length of password and raises an exception
        if password is too short
        
        :param username: checks if username belongs to an existing user and if
         and if so raises an exception userAlreadyExists
         
        :return: returns a user object if password length is ok and user
         doesn't exists.
        """
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)
        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False

