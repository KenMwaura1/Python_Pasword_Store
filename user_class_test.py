import unittest
from user_class import User


class UserTestCase(unittest.TestCase):
    def user_setup(self):
        """
        method to creates a new user that runs before the rest of the tests
        :return: new user
        """
        self.new_user = User("Zoo", "password123")



if __name__ == '__main__':
    unittest.main()
