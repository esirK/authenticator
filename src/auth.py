from src import Authenticator, Authorizor


class auth:
    authenticator = Authenticator()
    authorizor = Authorizor(authenticator)