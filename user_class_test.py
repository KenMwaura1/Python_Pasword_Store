import unittest
from user_class import User


class UserTestCase(unittest.TestCase):
    """
    class to define test cases for the User class
    """
    def setUp(self):
        """
        method to creates a new user that runs before the rest of the tests
        :return: new user
        """
        self.new_user = User("Zoo", "password123")

    def test_user_init(self):
        """
        test to ensure user is initialized properly
        :return: bool: True
        """
        self.assertEqual(self.new_user.username, "Zoo")
        self.assertEqual(self.new_user.password, "password123")

    def test_user_save(self):
        """
        test to check if a new user is added into User list
        :return: bool: True
        """
        self.new_user.add_user()
        self.assertEqual(len(User.list_of_users), 1)

    def test_display_all_contacts(self):
        """
        method that returns all contacts in the list
        :return: list of contacts
        """
        self.assertEqual(User.display_all_users(), User.list_of_users)


if __name__ == '__main__':
    unittest.main()
