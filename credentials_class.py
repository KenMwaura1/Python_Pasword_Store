import pyperclip
import random
import string


class Credentials:
    """
    Class to model and instantiate new credentials
    """
    list_of_credentials = []

    def __init__(self, username, password, account):
        """
        method to define properties of Credentials class
        """
        self.account = account
        self.username = username
        self.password = password

    def save_credentials(self):
        """
        method to store credentials in the list of credentials.
        :return: updated list of credentials
        """
        Credentials.list_of_credentials.append(self)
        return Credentials.list_of_credentials
