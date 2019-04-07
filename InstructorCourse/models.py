from django.db import models
from Course.models import Course
from Account.models import Account

# Create your models here.


class InstructorCourse(models.Model):
    Instructor = models.ForeignKey(Account, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Instructor) + " " + str(self.Course)
