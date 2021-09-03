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

    def tearDown(self):
        """
        test method to cleanup after each test is run
        :return: empty list of users
        """
        User.list_of_users = []

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

    def test_delete_contact(self):
        """
        Test whether we can remove a user from the list of users.
        :return: True if we can remove the contact
        """
        self.new_user.add_user()
        test_delete_user = User("Test", "passwd12")  # new user
        test_delete_user.add_user()
        self.new_user.delete_user()  # deletes user
        self.assertEqual(len(User.list_of_users), 1)

    def test_user_check(self):
        """
        Test to check if user exists in list of users
        :return: user
        """
        self.new_user.add_user()
        test_user = User("test", "pswd12")
        test_user.add_user()
        user_exists = User.user_check("test", "pswd12")
        self.assertTrue(user_exists)

if __name__ == '__main__':
    unittest.main()
