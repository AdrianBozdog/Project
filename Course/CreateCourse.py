from Course.models import Course
import re

class CreateCourse():

    def createCourse(self, command):

        if len(command) != 7:
            return "Your command is missing arguments, please enter your command in the following form: " \
                   "createCourse courseName courseNumber onCampus daysOfWeek start end"

        # Course number checks
        if not re.match('^[0-9]*$', command[2]):
            return "Course number must be numeric and three digits long"
        if len(command[2]) != 3:
            return "Course number must be numeric and three digits long"
        # Check that the course does not already exist
        if Course.objects.filter(number=command[2]).exists():
            return "Course already exists"
        # Location checks
        if command[3].lower() != "online" and command[3].lower() != "campus":
            return "Location is invalid, please enter campus or online."
        # Days check
        for i in command[4]:
            if i not in 'MTWRFN':
                return "Invalid days of the week, please enter days in the format: MWTRF or NN for online"
        # Check times
        startTime = command[5]
        endTime = command[6]
        if len(startTime) != 4 or len(endTime) != 4:
            return "Invalid start or end time, please use a 4 digit military time representation"
        if not re.match('^[0-2]*$', startTime[0]) or not re.match('^[0-1]*$', endTime[0]):
            return "Invalid start or end time, please use a 4 digit military time representation"
        for i in range (1,3):
            if not (re.match('^[0-9]*$', startTime[i])) or not (re.match('^[0-9]*$', endTime[i])):
                return "Invalid start or end time, please use a 4 digit military time representation"

        else:
            c = Course(name=command[1], number=command[2])
            if command[3].lower() == "online":
                c.onCampus = False
            else:
                c.onCampus = True
                c.classDays = command[4]
                c.classHoursStart = command[5]
                c.classHoursEnd = command[6]
            c.save()
            return "Course successfully created"
