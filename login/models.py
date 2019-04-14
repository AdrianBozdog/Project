from django.db import models
from Account.models import Account
# Create your models here


class LoginHelper():

    """
    Login takes a list of strings as arguments. It will take the name in command[1] and attempt to set that
    account as the Current User. If the argument list's length is greater or less than 3 an error
    string is returned. Exceptions are raised if the account was not found or the password was incorrect
    Login will return the title of the Current User if a login was successful
    """

    def login(self, command):

        test = Account.objects.filter(currentUser=True)
        # Accessing the login page will automatically log out previous user. This shouldn't ever happen but ill leave it.
        if len(test) > 0:
            raise Exception("A user is already logged in")
        if len(command) > 3 or len(command) < 3:
            raise Exception("Your command is missing arguments.  Please enter your command in the following format: login userName password")

        try:
            CurrentUser = Account.objects.get(userName=command[1])
            if CurrentUser.password != command[2]:
                raise Exception("Incorrect password")

        except Account.DoesNotExist:
            raise Exception("Account Not Found")

        CurrentUser.currentUser = True
        CurrentUser.save()
        return CurrentUser.title

    """
    Logout takes 0 arguments. If there is a Current User, that Accounts Current User flag is set to False.
    If a user was successfully logged out it will return True. If no account was logged in, it will return False
    """
    def logout(self):
        try:
            CurrentUser = Account.objects.get(currentUser=True)
            CurrentUser.currentUser = False
            CurrentUser.save()
            return True
        except Account.DoesNotExist:
            return False
        except Account.MultipleObjectsReturned:
            return False


