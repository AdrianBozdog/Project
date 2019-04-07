from CurrentUserHelper import CurrentUserHelper
from Account.models import Account
from Course.models import Course
from InstructorCourse.models import InstructorCourse


class assignInst():

    def assignInst(self, command):
        #cuh = CurrentUserHelper()
        #if cuh.getCurrentUserTitle() != 4:
        #   return "Permission denied. Only supervisors can assign instructor to courses"
        if len(command) < 3:
            return "Please, type the command in the following format assigninstructorcourse classNumber username"
        if not Course.objects.filter(number=command[2]).exists():
            return "Invalid course number"
        if not Account.objects.filter(userName=command[1]).exists():
            return "Invalid account name"
        instructor = Account.objects.get(userName=command[1])

        if instructor.title != 2:
            return "Account is not an instructor"

        course = Course.objects.get(userName=command[1])
        instructor = Account.objects.get(number=command[2])
        a = InstructorCourse()
        a.course = course
        a.instructor = instructor
        a.save()
        return "Assignment successfully completed"
