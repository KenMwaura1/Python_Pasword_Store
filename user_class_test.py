import unittest
from user_class import User


class UserTestCase(unittest.TestCase):
    def user_setup(self):
        """
        method to creates a new user that runs before the rest of the tests
        :return: new user
        """
        self.new_user = User("Zoo", "password123")

    def user_test_init(self):
        """
        test to ensure user is initialized properly
        :return: bool: True
        """
        self.assertEqual(self.new_user.username, "Zoo")
        self.assertEqual(self.new_user.password, "password123")

    def user_test_save(self):
        """
        test to check if a new user is added into User list
        :return: bool: True
        """
        self.new_user.add_user()
        self.assertEqual(len(User.list_of_users) , 1)


if __name__ == '__main__':
    unittest.main()
