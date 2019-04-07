from Account.models import Account


class LoginHelper():

    """
    Login takes a list of strings as arguments. It will take the name in command[1] and attempt to set that
    account as the Current User. If the argument list's length is greater or less than 3 an error
    string is returned. Error strings are returned if the Account was not found or the password is incorrect.
    """

    def login(self, command):

        test = Account.objects.filter(currentUser=True)
        if len(test) > 0:
            return "A user is already logged in"

        if len(command) > 3 or len(command) < 3:
            return "Your command is missing arguments.  Please enter your command in the following format: login userName password"

        try:
            CurrentUser = Account.objects.get(userName=command[1])
            if CurrentUser.password != command[2]:
                return "Incorrect password"

        except Account.DoesNotExist:
            return "Account Not Found"

        CurrentUser.currentUser = True
        CurrentUser.save()
        return "Logged in as " + command[1]

    """
    Logout takes 0 arguments. If there is a Current User, that Accounts Current User flag is set to False.
    If there is not a Current User, an error String is returned.  
    """
    def logout(self):
        try:
            CurrentUser = Account.objects.get(currentUser=True)
            CurrentUser.currentUser = False
            CurrentUser.save()
            return "Successfully logged out"
        except Account.DoesNotExist:
            return "Please log in First"
        except Account.MultipleObjectsReturned:
            return "Multiple account Logged in, Something went terribly wrong"


