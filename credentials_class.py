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

    def delete_credentials(self):
        """
        method to remove credentials from list of credentials.
        :return: removed credentials
        """
        Credentials.list_of_credentials.remove(self)
        return f"{self} account credentials removed"

    @classmethod
    def display_credentials(cls):
        """
        method to credentials currently in the list of credentials.
        :return: list of credentials
        """
        return cls.list_of_credentials

    @classmethod
    def search_credentials(cls, search_credentials: str):
        """
        method that takes the account (search_credentials) and searches for matching account in the list of credentials.
        :param search_credentials: str
        :return: credential if found in the list
        """
        for credential in cls.list_of_credentials:
            if credential.account == search_credentials:
                return credential.account
