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


if __name__ == '__main__':
    unittest.main()
