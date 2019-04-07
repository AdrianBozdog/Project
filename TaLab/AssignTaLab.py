from TaLab.models import TaLab
from Account.models import Account
from Lab.models import Lab
from Course.models import Course
from TACourse.models import TACourse


class AssignTaLab():

    """
    assignTaLab takes a list of strings as an argument. Command[1] is the Account username, Command[2] is the Course
    number and Command[3] is the Lab number. AssignTALAb creates  new TALab assignment if the account, lab, and course
    are all valid and the assignment doesn't already exist.
    """
    def assignTaLab(self, command):
        if len(command) < 4:
            return "Your argument is missing commands, please enter your command in the following format: " \
                   "assignTALab username classNumber labSectionNumber"

        if not Account.objects.filter(userName=command[1]).exists():
            return "Invalid account name"

        if not Course.objects.filter(number=command[2]).exists():
            return "Invalid course number"

        course = Course.objects.get(number=command[2])

        if not Lab.objects.filter(sectionNumber=command[3], course=course).exists():
            return "Invalid lab section"

        ta = Account.objects.get(userName=command[1])

        if ta.title > 1:
            return str(ta) + " is not a TA"

        if not TACourse.objects.filter(TA=ta, Course=Course.objects.get(number=command[2])).exists():
            return "TA must be assigned to the Course first"

        lab = Lab.objects.get(sectionNumber=command[3], course=course)

        if TaLab.objects.filter(Lab=lab).exists():
            return "Lab section already assigned"

        p = TaLab()
        p.TA = ta
        p.Lab = lab
        p.save()

        return "TA successfully assigned"

