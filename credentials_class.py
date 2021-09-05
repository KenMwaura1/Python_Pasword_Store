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
                return credential

    @classmethod
    def copy_credentials_password(cls, account_name: str):
        """
        Method to copy password to clipboard once found in list of credentials.
        :param account_name: str
        :return: password copied to clipboard.
        """
        found_credential = cls.search_credentials(account_name)
        pyperclip.copy(found_credential.password)

    @classmethod
    def copy_credentials_username(cls, account_name: str):
        """
        method to copy username to clipboard if it matches the one ib the list of credentials.
        :param account_name: str
        :return: username copied to clipboard
        """
        found_credential = cls.search_credentials(account_name)
        pyperclip.copy(found_credential.username)

    @classmethod
    def credential_exists(cls, account_name: str):
        """
        Method to check if a credential exists in the list of credentials.
        :param account_name: str
        :return: bool: True if it exists, False otherwise.
        """
        for credential in cls.list_of_credentials:
            return credential.account == account_name

    @classmethod
    def password_generator(cls, self=None):
        """
        method to generate a password using a combination of random characters consisting of digits, letters and special characters.
        :return: generated password
        """
        # if user specifies the length, its used.
        if self:
            password_length = self
        else:
            default_password_length = 10 # if no length is supplied the default is used
            password_length = default_password_length

        generator = string.ascii_lowercase + string.ascii_uppercase + string.digits + "~%!@^#$&*"
        password = "".join(random.choice(generator) for x in range(password_length))
        return password
