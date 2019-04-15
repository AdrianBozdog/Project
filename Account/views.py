from django.shortcuts import render
from django.views import View
from CurrentUserHelper import CurrentUserHelper
from Account.models import Account
# Create your views here.


class adminPage(View):

    def get(self, request):
        return render(request, 'Accounts/AdminHome.html')


class supervisorPage(View):

    def get(self, request):
        return render(request, 'Accounts/SupervisorHome.html')


class instructorPage(View):

    def get(self, request):
        CUH = CurrentUserHelper()
        Account = CUH.getCurrentUser()
        return render(request, 'Accounts/InstructorHome.html', {"Account": Account})

class taPage(View):

    def get(self, request):
        CUH = CurrentUserHelper()
        Account = CUH.getCurrentUser()
        return render(request, 'Accounts/TaHome.html', {"Account": Account})

class createAccountView(View):

    def get(self, request):
        accountList = list(Account.objects.all())
        return render(request, 'createAccount.html', {"accounts": accountList})

    def post(self, request):
        self.CA = Account()
        userName = str(request.POST["username"])
        firstName = str(request.POST["firstname"])
        lastName = str(request.POST["lastname"])
        email = str(request.POST["email"])
        title = str(request.POST["title"])

        command = [userName, title, email, firstName, lastName]

        try:
            message = Account.createAccountModels(self.CA, command)
            return render(request, 'createAccount.html', {"message": message})
        except Exception as e:
            return render(request, 'createAccount.html', {"message": str(e)})

