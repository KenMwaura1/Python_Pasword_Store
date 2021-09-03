import unittest
from credentials_class import Credentials


class CredentialsTestCase(unittest.TestCase):
    """
    Test class for the Credentials class.
    """
    def setUp(self) -> None:
        """
        method runs before each test
        :return: new User
        """
        self.new_credential = Credentials("Zoo", "password123", "Twitter")



if __name__ == '__main__':
    unittest.main()
