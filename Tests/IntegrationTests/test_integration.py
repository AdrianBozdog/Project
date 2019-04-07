from Account.models import Account
from LogIn import LoginHelper
from django.test import TestCase
from CurrentUserHelper import CurrentUserHelper
from Account.CreateAccount import CreateAccount
from Course.models import Course
from Course.CreateCourse import CreateCourse
from Lab.models import Lab
from Lab.CreateLab import CreateLab


class TestIntegration(TestCase):

    def setUp(self):
        self.login = LoginHelper()
        self.CUH = CurrentUserHelper()
        self.CA = CreateAccount()
        self.CC = CreateCourse()
        self.CL = CreateLab()
        self.account1 = Account.objects.create(firstName='Homer', userName='hsimpson', password='123456')
        self.account2 = Account.objects.create(firstName='Stu', userName='spidface', password='654321')
        self.course1 = Course.objects.create(name='Eng', number='101', onCampus='True', classDays='W')

    def test00(self):
        # test login
        self.assertEqual(self.login.login(["login", "Homer", "123456"]), "Account Not Found")

        self.assertFalse(self.CUH.isCurrent())

        self.assertEqual(self.login.login(["login", "hsimpson", "123456"]), "Logged in as hsimpson")

        self.assertTrue(self.CUH.isCurrent())

    def test01(self):
        # test login with logout
        self.assertFalse(self.CUH.isCurrent())

        self.assertEqual(self.login.login(["login", "hsimpson", '123456']), "Logged in as hsimpson")

        self.assertTrue(self.CUH.isCurrent())

        self.assertEqual(self.login.logout(), "Successfully logged out")

        self.assertFalse(self.CUH.isCurrent())

    def test02(self):
        # test create account login
        self.assertEqual(Account.objects.count(), 2)

        self.assertEqual(self.CA.createAccount(["createaccount", "taman", "ta", "what@uwm.edu"]),
                         "Account successfully created.  Temporary password is: taman456")

        self.assertEqual(Account.objects.count(), 3)

        self.assertFalse(self.CUH.isCurrent())

        self.assertEqual(self.login.login(["login", "taman", "taman456"]), "Logged in as taman")

        self.assertEqual(self.CUH.getCurrentUser(), Account.objects.get(userName='taman'))

        self.assertTrue(self.CUH.isCurrent())

        self.assertEqual(self.CUH.getCurrentUserTitle(), 1)

        self.assertEqual(self.login.logout(), "Successfully logged out")

        self.assertFalse(self.CUH.isCurrent())

    def test03(self):
        # test creating accounts with same username
        self.assertEqual(Account.objects.count(), 2)

        self.assertEqual(self.CA.createAccount(["createaccount", "hsimpson", "password", "what@uwm.edu"]), "Account already exists")

        self.assertEqual(Account.objects.count(), 2)

        self.assertEqual(self.CA.createAccount(["createaccount", "spidface", "password", "what@uwm.edu"]), "Account already exists")

        self.assertEqual(Account.objects.count(), 2)

    def test04(self):
        # test creating Courses
        self.assertEqual(Course.objects.count(), 1)

        self.assertEqual(self.CC.createCourse(["createCourse", "Eng", "101", "Campus", "TR", "1000", "1050"]), "Course already exists")

        self.assertEqual(Course.objects.count(), 1)

        self.assertEqual(self.CC.createCourse(["createCourse", "Eng", "102", "Campus", "TR", "1000", "1050"]), "Course successfully created")

        self.assertEqual(Course.objects.count(), 2)

    def test05(self):
        # test creating Labs
        self.assertEqual(Lab.objects.count(), 0)

        self.assertEqual(self.CL.createLab(["", "101", "801", "R", "1200", "1201"]), "Lab successfully created")

        self.assertEqual(Lab.objects.count(), 1)

        self.assertEqual(self.CL.createLab(["", "101", "801", "R", "1200", "1201"]), "Lab already exists, lab not added")

        self.assertEqual(Lab.objects.count(), 1)

    def test06(self):
        # test creating Labs and Courses

        self.assertEqual(Lab.objects.count(), 0)

        self.assertEqual(self.CL.createLab(["", "351", "801", "R", "1200", "1201"]), "The Course you are trying to create a lab for does not exist")

        self.assertEqual(Lab.objects.count(), 0)
        self.assertEqual(Course.objects.count(), 1)

        self.assertEqual(self.CC.createCourse(["createCourse", "DataStructures", "351", "Campus", "TR", "1000", "1050"]), "Course successfully created")

        self.assertEqual(Course.objects.count(), 2)

        self.assertEqual(self.CL.createLab(["", "351", "801", "R", "1200", "1201"]), "Lab successfully created")
        self.assertEqual(Lab.objects.count(), 1)

