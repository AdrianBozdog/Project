from Lab.models import Lab
from Course.models import Course
import re


class CreateLab:

    """
    CreateLab will create a lab given a list of strings, "command"
        command[0] = "createLab"
        command[1] = courseNumber of a course that exists in the database
        command[2] = sectionNumber for the lab
        command[3] = meeting days of lab
        command[4] = start time
        command[5] = end time

    If given valid input, the lab will be created and linked to the course it is for and the database
    will be updated. A confirmation message will be returned. If any arguments are invalid, an error message will be returned.
    """

    def createLab(self, command):
        if len(command) != 6:
            return "Your command is missing arguments, please enter your command in the following format: " \
                   "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime"

        courseNumber = command[1]
        sectionNumber = command[2]
        meetingDays = command[3]
        startTime = command[4]
        endTime = command[5]

        # Course number checks
        if not re.match('^[0-9]*$', courseNumber):
            return "Course number must be numeric and three digits long"
        if len(courseNumber) > 3 or len(courseNumber) < 3:
            return "Course number must be numeric and three digits long"

        # Make sure course that the lab is being created for exists
        try:
            c = Course.objects.get(number=courseNumber)
        except Course.DoesNotExist:
            return "The Course you are trying to create a lab for does not exist"

        # Make sure the course is not online
        if c.onCampus == False:
            return "You cannot create a lab for an online course"

        # Section number checks
        if not re.match('^[0-9]*$', sectionNumber):
            return "Section number must be numeric and three digits long"
        if len(sectionNumber) > 3 or len(sectionNumber) < 3:
            return "Section number must be numeric and three digits long"

        # Days check
        for i in meetingDays:
            if i not in 'MTWRFN':
                return "Invalid days of the week, please enter days in the format: MWTRF"

        # Time checks
        if len(startTime) != 4 or len(endTime) != 4:
            return "Invalid start or end time, please use a 4 digit military time representation"
        if not re.match('^[0-2]*$', startTime[0]) or not re.match('^[0-2]*$', endTime[0]):
            return "Invalid start or end time, please use a 4 digit military time representation"
        for i in range(1, 3):
            if not (re.match('^[0-9]*$', startTime[i])) or not (re.match('^[0-9]*$', endTime[i])):
                return "Invalid start or end time, please use a 4 digit military time representation"

        # Make sure the lab does not already exist
        if Lab.objects.filter(course=c, sectionNumber=sectionNumber).exists():
            return "Lab already exists, lab not added"
        else:
            l = Lab.objects.create(course=c)
            l.sectionNumber = sectionNumber
            l.meetingDays = meetingDays
            l.startTime = startTime
            l.endTime = endTime
            l.save()
            return "Lab successfully created"
