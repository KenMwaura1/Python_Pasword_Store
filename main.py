#!/home/zoo/Documents/Moringa-projects/Python_Pasword_Store/venv/bin/python
from credentials_class import Credentials
from user_class import User
import typer


def create_new_user(username: str, password: str):
    """
    function to create a new User instance passing along username and password.
    :param username: str
    :param password: str
    :return: new user
    """
    return User(username, password)


def save_user(new_user: User):
    """
    function to save new user to the list of users
    :param new_user: User
    :return: user added to list of users
    """
    new_user.add_user()


def show_user():
    """
    function to show existing users
    :return: existing users
    """
    return User.display_all_users()


def user_login(username: str, password: str):
    """
    function to login user once its confirmed they exist
    :param username: str
    :param password: str
    :return: verified user
    """
    return User.user_check(username, password)


def create_new_credentials(username: str, password: str, account_name: str):
    """
    function to create new credentials for specified user
    :param username: string
    :param password: string
    :param account_name: string
    :return: new credentials
    """
    return Credentials(username, password, account_name)


def save_credentials(credentials: Credentials):
    """
    function to save credentials to list of credentials
    :param credentials:
    :return: updated credentials list
    """
    credentials.save_credentials()


def display_credentials():
    """
    function to display saved credentials
    :return: list of saved credentials
    """
    return Credentials.display_credentials()


def delete_credentials(credentials):
    """
    function to delete credentials from list of credentials
    :param credentials:
    :return: delete_credentials
    """
    Credentials.delete_credentials(credentials)

def main():
    """

    :return:
    """
    typer.secho("Zoo Password Locker", fg=typer.colors.BRIGHT_MAGENTA,
                underline=True, bold=True, blink=True, reverse=True)


if __name__ == '__main__':
    main()
