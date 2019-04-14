from TACourse.models import TACourse
from Account.models import Account
from Course.models import Course


class AssignTACourse:
    """
    assignTACourse takes a list of strings, "command"
        command[0] = "assignTACourse"
        command[1] = userName of a TA that exists in the database
        command[2] = courseNumber of a course that exists in the database

    If the username and course number are valid, the TA will be assigned to the course and the database
    will be updated. A confirmation message will be returned. If any arguments are invalid, an error message will be returned.
    """

    def assignTACourse(self, command):

        # the number of arguments must be 3
        if len(command) != 3:
            return "Your command has an incorrect number of arguments, please enter your command in the following format: " \
                   "assignTACourse userName classNumber"

        # search database for given username to make sure the account exists
        if not Account.objects.filter(userName=command[1]).exists():
            return "Invalid TA username."

        # search database for given course number to make sure the course exists
        if not Course.objects.filter(number=command[2]).exists():
            return "Invalid course number."

        ta = Account.objects.get(userName=command[1])

        # title designates privileges; 1 for TA. Make sure account with given username is a TA.
        if ta.title > 1:
            return "Account is not a TA."

        course = Course.objects.get(number=command[2])

        # Look for the TA assignment to see if the TA is already assigned to the course.
        if TACourse.objects.filter(TA=ta, Course=course).exists():
            return str(ta) + " is already assigned to " + str(course)

        # No errors--can go ahead and assign
        l = TACourse()
        l.TA = ta
        l.Course = course
        l.save()

        return "Assignment successful."
