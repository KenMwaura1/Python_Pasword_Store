class User:
    """
    This is the user class used model instances of new users
    """
    list_of_users = []

    def __init__(self, username: str, password: str):
        """
        init method to define Users properties
        :param username:
        :param password:
        """
        self.username = username
        self.password = password

    def add_user(self):
        """
        User method to add user to list of users
        :return: list of users
        """
        User.list_of_users.append(self)

    def delete_user(self):
        """
        remove user from the current list of users
        :return: removed user
        """
        User.list_of_users.remove(self)
        return f"{self} removed from the list"

    @classmethod
    def display_all_users(cls):
        """
        method to display users currently in the list of users
        :return: list of users
        """
        return cls.list_of_users



