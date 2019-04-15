from django.shortcuts import render
from django.views import View
from Account.models import Account
from ViewCourseAssign.models import viewTaAssignments, viewAllTaAssignments
# Create your views here.


class viewTaAssign(View):

    def get(self, request):
        taList = Account.objects.filter(title=1)
        return render(request, 'viewAssignments.html', {"taList": taList})

    def post(self, request):
        taList = Account.objects.filter(title=1)
        account = str(request.POST["taAccount"])
        allAssignments = []
        assignment = ""
        if account == "all":
            allAssignments = viewAllTaAssignments()
        else:
            command = ["", account]

            assignment = viewTaAssignments(command)

        return render(request, 'viewAssignments.html', {"assignments": assignment, "taList": taList, "allassignments": allAssignments})
