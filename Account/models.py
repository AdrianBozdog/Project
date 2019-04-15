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


    def createAccountModels(self, command):

        # Check that the account trying to be created does not already exist
        if Account.objects.filter(userName=command[0]).exists():
            raise Exception("Account already exists")

        # Make sure the account is trying to be created with a UWM email address
        str = command[2].split('@', 1)
        if len(str) == 1:
            raise Exception("The email address you have entered in not valid.  "
                   "Please make sure you are using a uwm email address in the correct format.")
        if str[1] != "uwm.edu":
            raise Exception("The email address you have entered in not valid.  "
                   "Please make sure you are using a uwm email address in the correct format.")

        # If we get here the account is safe to be created.
        else:
            A = Account()
            A.userName = command[0]
            A.email = command[2]
            A.firstName = command[3]
            A.lastName = command[4]
            if command[1].lower() == "ta":
                A.title = 1
            elif command[1].lower() == "instructor":
                A.title = 2
            else:
                raise Exception("Invalid title, account not created")

            # Make a temporary password for the newly created user
            A.password = A.userName + "456"
            A.save()

            return "Account successfully created.  Temporary password is: " + A.userName + "456"