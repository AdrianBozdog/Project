from Account.models import Account
from TaLab.models import TaLab
from InstructorCourse.models import InstructorCourse
from TACourse.models import TACourse
# Create your models here.


class viewCourseAssign():
    """
    ViewCourseAssign takes a list of strings as an arguments. Command[1] is the account userName. If the account
    is a valid TA or Instructor account, viewCrouseAssign will return a string containing a comma separated list of all
    of the Courses and Lab sections that the Account is assigned to.
    """
    def viewCourseAssign(self, command):

        if len(command) < 2:
            return "Please enter the userName of the Account"

        if not Account.objects.filter(userName=command[1]).exists():
            return "Account not found"

        account = Account.objects.get(userName=command[1])

        if account.title is 2:
            if not InstructorCourse.objects.filter(Instructor=account).exists():
                return str(account) + " does not have any assignments"

            assignments = InstructorCourse.objects.filter(Instructor=account)

            response = str(account) + " is assigned to: "
            courseList = []
            for a in assignments:
                courseList.append(str(a.Course))

            response += ", ".join(courseList)

            return response
        elif account.title is 1:
            if not TACourse.objects.filter(TA=account).exists():
                return str(account) + " does not have any assignments"

            labAssignments = TaLab.objects.filter(TA=account)

            response = str(account) + " is assigned to: "
            labList = []
            checkList = []
            for a in labAssignments:
                labList.append(str(a.Lab))
                checkList.append(a.Lab.course)

            response += ", ".join(labList)

            courseAssignments = TACourse.objects.filter(TA=account)

            courseList = []
            first = True
            for a in courseAssignments:
                if a.Course not in checkList:
                    if first and len(labAssignments) != 0:# all this does is puts a comma after lab sections if present
                        response += ", "
                        first = False
                    courseList.append(str(a.Course))

            response += ", ".join(courseList)

            return response

        else:
            return "Only Ta and Instructor accounts can have Assignments"
