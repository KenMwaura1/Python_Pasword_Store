import unittest
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

if __name__ == '__main__':
    unittest.main()
