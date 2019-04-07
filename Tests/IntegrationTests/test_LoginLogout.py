from Account.models import Account
from LogIn import LoginHelper
from django.test import TestCase
from CurrentUserHelper import CurrentUserHelper


class TestLoginLogout(TestCase):

    def setUp(self):
        self.login = LoginHelper()
        self.CUH = CurrentUserHelper()
        Account.objects.create(firstName='Homer', userName='hsimpson', password='123456')
        Account.objects.create(firstName='Stu', userName='spidface', password='654321')

    def test00(self):
        self.assertEqual(self.login.login(["login", "Homer", "123456"]), "Account Not Found")

        self.assertFalse(self.CUH.isCurrent())

        self.assertEqual(self.login.login(["login", "hsimpson", "123456"]), "Logged in as hsimpson")

        self.assertTrue(self.CUH.isCurrent())

    def test01(self):
        self.assertFalse(self.CUH.isCurrent())

        self.assertEqual(self.login.login(["login", "hsimpson", '123456']), "Logged in as hsimpson")

        self.assertTrue(self.CUH.isCurrent())

        self.assertEqual(self.login.logout(), "Successfully logged out")

        self.assertFalse(self.CUH.isCurrent())
