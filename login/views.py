from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from login.models import LoginHelper
# Create your views here.


class loginPage(View):

    def get(self, request):
        LH = LoginHelper()
        LH.logout()
        return render(request, 'loginscreen.html')

    def post(self, request):
        LH = LoginHelper()
        LH.logout()
        username = str(request.POST["username"])
        password = str(request.POST["password"])
        username = username.strip()
        command = ["", username, password]

        try:
            check = LH.login(command)

            if check == 1:
                return redirect('/ta/')
            if check == 2:
                return redirect('/instructor/')
            if check == 3:
                return redirect('/administrator/')
            if check == 4:
                return redirect('/supervisor/')

        except Exception as e:

            return render(request, 'loginscreen.html', {"message": str(e)})

