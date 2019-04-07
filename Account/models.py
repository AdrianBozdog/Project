from django.db import models

# Create your models here.


class Account(models.Model):
    userName = models.CharField(max_length=20, default=" ")
    firstName = models.CharField(max_length=20, default=" ")
    lastName = models.CharField(max_length=20, default=" ")
    password = models.CharField(max_length=20, default="password")
    email = models.EmailField(default="")
    title = models.IntegerField(default=0)
    address = models.CharField(max_length=30, default=" ")
    city = models.CharField(max_length=20, default=" ")
    state = models.CharField(max_length=20, default=" ")
    zipCode = models.IntegerField(default=00000)
    officeNumber = models.IntegerField(default=000)
    officePhone = models.CharField(max_length=12, default="000-000-0000")
    officeDays = models.CharField(max_length=10, default=" ")
    officeHoursStart = models.IntegerField(default=0000)
    officeHoursEnd = models.IntegerField(default=0000)
    currentUser = models.BooleanField(default=False)
    
    def __str__(self):
        return self.userName


