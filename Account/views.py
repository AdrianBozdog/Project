from django.shortcuts import render
from django.views import View
from CurrentUserHelper import CurrentUserHelper
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
