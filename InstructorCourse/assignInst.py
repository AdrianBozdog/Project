from Account.models import Account
from Course.models import Course
from InstructorCourse.models import InstructorCourse


class assignInst:

    """
    This class is for command of assign instructor to course
    assignInst will take in a list of strings, "command"
        command[0] = "assigninstructorcourse"
        command[1] = userName of an instructor with an existing account
        command[2] = courseNumber of an existing course

    If the arguments are valid, the assignment will be successful and the database will be updated. A confirmation
    message will be returned. If any arguments are invalid, an error message will be returned.
    """

    def assignInst(self, command):
        # Check if there are 3 arguments
        if len(command) != 3:
            return "There are arguments missing, Please enter your command in the following format: "\
                    "assigninstructorcourse userName courseNumber"
        # Check if the course is valid
        if not Course.objects.filter(number=command[2]).exists():
            return "Invalid course number"
        # Check if the user name is valid
        if not Account.objects.filter(userName=command[1]).exists():
            return "Invalid user name"

        instructor = Account.objects.get(userName=command[1])
        course = Course.objects.get(number=command[2])
        # title represented as an integer where 4=supervisor 3=administrator
        # 2=Instructor 1=TA. 0=No current User
        # Check if the account is an instructor
        if instructor.title != 2:
            return "Account is not an instructor"
        # Check if the course is already assigned
        if InstructorCourse.objects.filter(Course=course).exists():
            return "This class is already assigned"
        # Otherwise(if there are no errors found), an instructor can be assigned to a course
        else:
            a = InstructorCourse()
            a.Instructor = instructor
            a.Course = course
            a.save()
            return "Instructor was successfully assigned to class"
