"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from main import views as main
from login import views as login
from Account import views as account
from ViewCourseAssign import views as vca
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", login.redirect_view),
    path("command/", main.Home.as_view()),
    path("login/", login.loginPage.as_view()),
    path("administrator/", account.adminPage.as_view()),
    path("supervisor/", account.supervisorPage.as_view()),
    path("instructor/", account.instructorPage.as_view()),
    path("ta/", account.taPage.as_view()),
    path("createaccount/", account.createAccountView.as_view()),
    path("viewtaassignments/", vca.viewTaAssign.as_view())
]

urlpatterns += staticfiles_urlpatterns()