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



def main():
    """

    :return:
    """
    typer.secho("Zoo Password Locker", fg=typer.colors.BRIGHT_MAGENTA,
                underline=True, bold=True, blink=True, reverse=True)


if __name__ == '__main__':
    main()
