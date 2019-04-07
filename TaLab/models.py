from django.db import models
from Account.models import Account
from Lab.models import Lab
# Create your models here.


class TaLab(models.Model):
    TA = models.ForeignKey(Account, on_delete=models.CASCADE)
    Lab = models.ForeignKey(Lab, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.TA) + " " + str(self.Lab)
