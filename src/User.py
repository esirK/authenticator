import hashlib


class User:
    def __init__(self, username, password):
        """Create A new User Object,The password will be encrypted 
        before storing .
        """
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        """"Encrypt the password with username and return  the 
        sha digest. 
        """
        hash_string = (self.username+password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """
        :param password: 
        :return true is password matches current user false otherwise:
        """
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password
