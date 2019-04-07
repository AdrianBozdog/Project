from Account.models import Account
from Course.models import Course
from InstructorCourse.models import InstructorCourse


class assignInst():

    def assignInst(self, command):
        if len(command) != 3:
            return "Your argument is missing commands, " \
                   "please enter your command in the following format: assigninstructorcourse userName courseNumber"
        if not Course.objects.filter(number=command[2]).exists():
            return "Invalid course number"
        if not Account.objects.filter(userName=command[1]).exists():
            return "Invalid user name"

        instructor = Account.objects.get(userName=command[1])
        course = Course.objects.get(number=command[2])

        if instructor.title != 2:
            return "Account is not an instructor"

        if InstructorCourse.objects.filter(Course=course).exists():
            return "This class was already assigned"
        else:
            a = InstructorCourse()
            a.Instructor = instructor
            a.Course = course
            a.save()
            return "Instructor was successfully assigned to class"
