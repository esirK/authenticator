from src.AuthException import InvalidUsername, NotLoggedInError, NotPermittedError


class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, permission_name):
        """
    
        :param permission_name: 
        :return: Create a new Permission that users can be added to 
        """
        try:
            perm_set = self.permissions[permission_name]
        except KeyError:
            self.permissions[permission_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        """
        
        :param perm_name: 
        :param username: 
        :return Grant the user specified by username the specified permission  
        """
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission Does Not Exists")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permissions(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission Does Not Exists")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True


