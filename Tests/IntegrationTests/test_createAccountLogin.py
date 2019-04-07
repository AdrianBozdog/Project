from Account.models import Account
from LogIn import LoginHelper
from django.test import TestCase
from CurrentUserHelper import CurrentUserHelper
from Account.CreateAccount import CreateAccount


class TestCreateAccountLogin(TestCase):

    def setUp(self):
        self.CUH = CurrentUserHelper()
        self.CA = CreateAccount()
        self.LH = LoginHelper()

    def test00(self):
        self.assertEqual(self.CA.createAccount(["createaccount", "hsimpson", "ta", "what@uwm.edu"]), "Account successfully created")

        self.assertFalse(self.CUH.isCurrent())

        self.assertEqual(self.LH.login(["login", "hsimpson", "password"]),"Logged in as hsimpson")

        self.assertTrue(self.CUH.isCurrent())

        self.assertEqual(self.CUH.getCurrentUserTitle(), 1)

        self.assertEqual(self.CUH.getCurrentUser(), Account.objects.get())

        self.assertEqual(self.LH.logout(), "Successfully logged out")

        self.assertFalse(self.CUH.isCurrent())
