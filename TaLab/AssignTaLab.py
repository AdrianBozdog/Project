from TaLab.models import TaLab
from Account.models import Account
from Lab.models import Lab
from Course.models import Course


class AssignTaLab():

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
            return "Account is not a ta"

        lab = Lab.objects.get(sectionNumber=command[3], course=course)

        if TaLab.objects.filter(Lab=lab).exists():
            return "Lab section already assigned"

        p = TaLab()
        p.TA = ta
        p.Lab = lab
        p.save()

        return "TA successfully assigned"

