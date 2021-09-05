import unittest

import pyperclip

from credentials_class import Credentials


class CredentialsTestCase(unittest.TestCase):
    """
    Test class for the Credentials class.
    """

    def setUp(self) -> None:
        """
        method runs before each test
        :return: new Credentials object
        """
        self.new_credential = Credentials("Zoo", "password123", "Twitter")

    def tearDown(self) -> None:
        """
        cleans up after each Test case is run
        :return: empty credentials list
        """
        Credentials.list_of_credentials = []

    def test_init(self):
        """
        Test case if Credentials is appropriately initialized.
        :return: bool True
        """
        self.assertEqual(self.new_credential.username, "Zoo")
        self.assertEqual(self.new_credential.password, "password123")
        self.assertEqual(self.new_credential.account, "Twitter")

    def test_credential_save(self):
        """
        Test case to check if credential object is saved to credentials list
        :return: True if item is saved to list
        """
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.list_of_credentials), 1)

    def test_credential_delete_(self):
        """
        Test to check if we can remove account credentials from list of credentials
        :return: Bool: True
        """
        self.new_credential.save_credentials()
        test_credential_delete = Credentials("Zoo", "pwd1234", "Twitter")
        test_credential_delete.save_credentials()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.list_of_credentials), 1)

    def test_credentials_save_multiple_credentials(self):
        """
        Test if can add multiple credentials to the list of credentials.
        :return: Bool: True if we can add multiple credentials to the list of credentials
        """
        self.new_credential.save_credentials()
        test_credentials_save_multiple_credentials = Credentials("Zoov", "pxz1234", "Instagram")
        test_credentials_save_multiple_credentials.save_credentials()
        self.assertEqual(len(Credentials.list_of_credentials), 2)

    def test_display_credentials(self):
        """
        Test to return the credentials currently in list_of_credentials
        :return: current credentials saved
        """
        self.assertEqual(Credentials.display_credentials(), Credentials.list_of_credentials)

    def test_find_credentials(self):
        """
        Test to find credentials in list_of_credentials from account passed as search string
        :return: Bool: True if account matches the one in the list
        """
        self.new_credential.save_credentials()
        test_find_credentials = Credentials("zoocodes", "pwsds123", "Twitter")
        test_find_credentials.save_credentials()
        found_credential = Credentials.search_credentials("Twitter")
        self.assertEqual(found_credential.account, test_find_credentials.account)

    def test_copy_password(self):
        """
        Test to see we can copy password from list_of_credentials
        :return: Bool: True
        """
        self.new_credential.save_credentials()
        test_copy_password = Credentials("test", "pswd123", "LinkedIn")
        test_copy_password.save_credentials()
        found_password = test_copy_password.copy_credentials_password("LinkedIn")
        self.assertEqual(test_copy_password.password, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
