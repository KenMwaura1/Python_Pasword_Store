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


def check_credentials(account_name: str):
    """
    function to check if credentials exist in the list of credentials
    :param account_name: string
    :return: bool True if found,
    """
    return Credentials.credential_exists(account_name)


def find_credentials(account_name: str):
    """
    function that takes an account name and returns the resultant credentials
    :param account_name: string
    :return: credentials of the search term
    """
    return Credentials.search_credentials(account_name)


def password_generator(password_length=None):
    """
    function to generate password for the user
    :param password_length: int
    :return: generated password
    """
    return Credentials.password_generator(password_length)


def password_copy(account_name: str):
    """
    function that takes an account name and copies the password to the clipboard using Pyperclip
    :param account_name: string
    :return: password copied to clipboard
    """
    return Credentials.copy_credentials_password(account_name)


def username_copy(account_name: str):
    """
     function that takes an account name and copies the username to the clipboard using Pyperclip
    :param account_name:string
    :return: username copied to clipboard
    """
    return Credentials.copy_credentials_username(account_name)


def main():
    """
    main function to display texts and accepts inputs.
    :return:
    """
    typer.secho("Zoo Password Locker", fg=typer.colors.BRIGHT_MAGENTA,
                underline=True, bold=True, blink=True, reverse=True)

    typer.secho("Welcome to Zoo Password Locker \n \n Please type one of following shortcodes: \n"
                f"CU " + '-' * 5 + "Create New User" + "\n \n EU " + "-" * 5 + " Existing User \n",
                fg=typer.colors.BRIGHT_YELLOW)

    user_shortcode = input("").strip().lower()
    if user_shortcode == "cu":
        def create_new_user_():
            typer.secho("Register", bg=typer.colors.BRIGHT_GREEN, fg=typer.colors.BRIGHT_WHITE)
            typer.secho("*^" * 30, fg=typer.colors.BRIGHT_CYAN)
            username = input("Enter your username: ")
            while True:
                typer.secho("*" * 10, fg=typer.colors.BRIGHT_GREEN)
                typer.secho("Select one of the following: \n \n UP --- To enter your own password "
                            "\n AP --- To get a Automated generated password")
                password_select = input().strip().lower()
                if password_select == "up":
                    password = input("Enter your password \n")
                    break
                elif password_select == "ap":
                    typer.secho("Enter the preferred length of the generated password, default is 10")
                    password_length = int(input())
                    password = password_generator(password_length)
                    break
                else:
                    typer.secho("Invalid Option selected, Kindly try again.", bg=typer.colors.BRIGHT_RED)
            save_user(create_new_user(username, password))
            typer.secho("##" * 40, fg=typer.colors.BRIGHT_GREEN)
            typer.secho(f"Congratulations {username}, your account created successfully. Your Password is: {password}",
                        fg=typer.colors.BRIGHT_BLUE)
            typer.secho("##" * 40, fg=typer.colors.BRIGHT_GREEN)

        create_new_user_()

    elif user_shortcode == "eu":
        typer.secho("^^" * 40, fg=typer.colors.BRIGHT_GREEN)
        typer.secho(" Enter your username and password to sign in: \n ", fg=typer.colors.BRIGHT_MAGENTA)
        typer.secho("~~" * 40, fg=typer.colors.BRIGHT_GREEN)
        username = input(" Username --> : ")
        password = input(" Password --> : ")
        sign_in = user_login(username, password)
        if user_login == sign_in:
            typer.secho(f"Hey {username}. Welcome back! \n")

    while True:
        typer.secho("Select One of these shortcodes: \n CA ---> Create new account \n DA ---> Display Accounts \n"
                    "FA ---> Find an Existing Account \n DA ---> Delete Account \n PG ---> Generate a random password "
                    "\n EX ---> Exit the Password Locker ")
        user_selection = input().strip().lower()
        if user_selection == "ca":
            typer.secho("Create New Credential", fg=typer.colors.BRIGHT_MAGENTA)
            typer.secho("@" * 40, fg=typer.colors.YELLOW)
            typer.secho("Account name ....", fg=typer.colors.BRIGHT_MAGENTA)
            account = input().lower()
            typer.secho("Your Account username", fg=typer.colors.BRIGHT_MAGENTA)
            username = input()
            while True:
                typer.secho("Select one of the following: \n \n UP --- To enter your own password "
                            "\n AP --- To get a Automated generated password", fg=typer.colors.BRIGHT_RED)
                password_select = input().strip().lower()
                if password_select == "up":
                    password = input("Enter your own password:  \n ")
                    break
                elif password_select == "ap":
                    typer.secho("Enter the preferred length of the generated password, default is 10")
                    password_length = int(input())
                    password = password_generator(password_length)
                    break
                else:
                    typer.secho("Invalid Option selected, Kindly try again.", bg=typer.colors.BRIGHT_RED)
                save_credentials(create_new_credentials(account, username, password))
                typer.secho(f"\n Account details  username:{username}, password:{password} "
                            f"and account:{account} saved successfully  ")
        elif user_selection == "da":
            if display_credentials():
                typer.secho("Below is a list of accounts: ", fg=typer.colors.BRIGHT_MAGENTA)
                typer.secho("++" * 40, fg=typer.colors.BRIGHT_BLUE)
                for credential in display_credentials():
                    typer.secho(f"Account: {credential.account} --> username: {credential.username} "
                                f"--> password: {credential.password}", fg=typer.colors.BRIGHT_CYAN)
                    typer.secho("``" * 30)
                typer.secho("++" * 40, fg=typer.colors.BRIGHT_BLUE)
            else:
                typer.secho("No Accounts saved currently", bg=typer.colors.BRIGHT_RED)
        elif user_selection == "fa":
            typer.secho("Enter the name of the account to search", fg=typer.colors.BRIGHT_YELLOW)
            search_term = input().strip().lower()
            if find_credentials(search_term):
                search_account = find_credentials(search_term)
                typer.secho(f"Account: {search_account}", fg=typer.colors.BRIGHT_GREEN)
                typer.secho("**" * 40, fg=typer.colors.BRIGHT_BLUE)
                typer.secho(f"User Name: {search_account.username}, Password: {search_account.password}")
                typer.secho("**" * 40, fg=typer.colors.BRIGHT_BLUE)
            else:
                typer.secho("Account not found \n")

        elif user_selection == "da":
            typer.secho("Enter the account to delete : ", bg=typer.colors.BRIGHT_RED)
            delete_credential = input().strip().lower()
            if find_credentials(delete_credential):
                account_search = find_credentials(delete_credential)
                account_search.delete_credentials()
                typer.secho(f"\n Account credentials for {account_search.account} deleted successfully \n",
                            fg=typer.colors.BRIGHT_RED)
            else:
                typer.secho(f" \n Account credentials not found for {delete_credential} \n", bg=typer.colors.YELLOW)

        elif user_selection == "pg":
            auto_password_length = int(input("enter your preferred password length, default=10").strip())
            if auto_password_length == "":
                auto_password = password_generator(10)
            else:
                auto_password = password_generator(auto_password_length)
            typer.secho(f"Password: {auto_password} generated successfully. Add it to your account.",
                        fg=typer.colors.BRIGHT_GREEN)
        elif user_selection == "ex":
            typer.secho("Thank you for using Zoo Password Store! ")
            break
        else:
            typer.secho("Selection not in list, Kindly confirm and try again", bg=typer.colors.BRIGHT_RED)
    else:
        typer.secho("Please select a valid input to continue")


if __name__ == '__main__':
    main()
