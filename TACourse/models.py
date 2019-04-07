from django.db import models
from Account.models import Account
from Course.models import Course

# Create your models here.


class TACourse(models.Model):
    TA = models.ForeignKey(Account, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.TA) + " " + str(self.Course)
