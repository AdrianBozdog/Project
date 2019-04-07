from Account.models import Account
from random import randint


class CreateAccount():

    def createAccount(self, command):

        # Check that the command has the correct number of arguments
        if len(command) > 4 or len(command) < 4:
            return "Your command is missing arguments, please enter your command in the following format: " \
                   "createAccount username title email"

        # Check that the account trying to be created does not already exist
        if Account.objects.filter(userName=command[1]).exists():
            return "Account already exists"

        # Make sure the account is trying to be created with a UWM email address
        str = command[3].split('@', 1)
        if len(str) == 1:
            return "The email address you have entered in not valid.  " \
                   "Please make sure you are using a uwm email address in the correct format."
        if str[1] != "uwm.edu":
            return "The email address you have entered in not valid.  " \
                    "Please make sure you are using a uwm email address in the correct format."
        else:
            A = Account()
            A.userName = command[1]
            A.email = command[3]
            if command[2].lower() == "ta":
                A.title = 1
            elif command[2].lower() == "instructor":
                A.title = 2
            else:
                return "Invalid title, account not created"

            A.password=A.userName + "456"
            A.save()

            return "Account successfully created.  Temporary password is: " + A.userName + "456"

