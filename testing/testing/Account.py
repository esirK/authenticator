from testing.testing.ConnectionError import ConnectionsError
import requests


class Account:
    def __init__(self, data_interface):
        self.di = data_interface

    def get_account(self, id_num):
        """
        :param id_num: the id number of a specific account in database 
        :return: data obtained from the database for the given id
        """
        try:
            result = self.di.get(id_num)
        except ConnectionsError:
            result = "Connection error occurred. Try again latter"
        return result

    def get_account_balance(self, id_num):
        """
        
        :param id_num: of the account holder 
        :return: amount in id_num account
        """
        response = requests.get("http://somefuckedupshit/"+id_num)
        return {'status': response.status_code, 'data': response.text}
