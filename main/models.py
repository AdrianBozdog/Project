from Account.models import Account
from LogIn import LoginHelper
from Account.CreateAccount import CreateAccount
from Lab.CreateLab import CreateLab
from Course.CreateCourse import CreateCourse
from CurrentUserHelper import CurrentUserHelper
from TaLab.AssignTaLab import AssignTaLab
# Create your models here.


class UI:
    """
    Here is where the string input from the command line is parsed. I currently have it set up so its
    checking the string in lower so that the commands wont be case sensitive. If you wish to add an additional
    command just add another "elif command[0].lower() == <commandName>" at the bottom. Make sure command
    returns a string.
    """

    def command(self, inStr):
        command = inStr.split(' ')

        if command[0].lower() == "login":
            login = LoginHelper()
            return login.login(command)

        elif command[0].lower() == "logout":
            logout = LoginHelper()
            return logout.logout()

        elif command[0].lower() == "createaccount":
            CUH = CurrentUserHelper()
            if CUH.getCurrentUserTitle() < 3:
                return "You do not have the credentials to create an account. Permission denied"

            CA = CreateAccount()
            return CA.createAccount(command)

        elif command[0].lower() == "createlab":
            CUH = CurrentUserHelper()
            if CUH.getCurrentUserTitle() < 3:
                return "You do not have the credentials to create a lab. Permission denied"

            create = CreateLab()
            return create.createLab(command)

        elif command[0].lower() == "createcourse":
            CUH = CurrentUserHelper()
            if CUH.getCurrentUserTitle() < 3:
                return "You do not have the credentials to create a course. Permission denied"

            create = CreateCourse()
            return create.createCourse(command)

        elif command[0].lower() == "assigninstructorcourse":
            CUH = CurrentUserHelper()
            if CUH.getCurrentUserTitle() < 3:
                return "You do not have the credentials to assign an instructor to a course. Permission denied"

            return command[0]

        elif command[0].lower() == "assigntalab":
            CUH = CurrentUserHelper()
            if CUH.getCurrentUserTitle() < 2:
                return "You do not have the credentials to assign a ta to a lab. Permission denied"

            atl = AssignTaLab()

            return atl.assignTaLab(command)

        elif command[0].lower == "assigntacourse":
            CUH = CurrentUserHelper()
            if CUH.getCurrentUserTitle() < 3:
                return "You do not have the credentials to assign a ta to a course. Permission denied"

            return command[0]

        elif command[0].lower == "viewcourseassign":
            return command[0]

        else:
            return command[0] + " is an unsupported command"

        return "No command was executed, something went terribly wrong"




