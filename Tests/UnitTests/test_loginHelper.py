from django.test import TestCase
from Account.models import Account
from LogIn import LoginHelper


class TestLoginHelper(TestCase):

    def setUp(self):
        Account.objects.create(userName='hsimpson', password='password', firstName='homer')
        self.login = LoginHelper()
        self.Command1 = ["login", "hsimpson", "password"]
        self.Command2 = ["login", "hsimpson", "wrongPassword"]
        self.Command3 = ["login", "rob", "password"]
        self.Command4 = ["login", "hsimpson"]
        self.Command5 = ["login", "hsimpson", "password", "something"]

    def test_login_success(self):
        #test Successful login
        self.assertEqual(self.login.login(self.Command1), "Logged in as homer")
        A = Account.objects.get(firstName='homer')
        Account.objects.exists()
        self.assertTrue(A.currentUser)

    def test_login_wrong_password(self):
        # test wrong password
        self.assertEqual(self.login.login(self.Command2), "Incorrect password")

        with self.assertRaises(Account.DoesNotExist):
            A = Account.objects.get(currentUser='True')

    def test_login_account_not_found(self):
        #test logging in with an Account not in the database
        self.assertEqual(self.login.login(self.Command3), "Account Not Found")

        with self.assertRaises(Account.DoesNotExist):
            A = Account.objects.get(currentUser='True')

    def test_login_2_arguments(self):
        #User doesn't enter enough arugments
        self.assertEqual(self.login.login(self.Command4), "Your command is missing arguments.  Please enter your command in the following format: login userName password")

        with self.assertRaises(Account.DoesNotExist):
            A = Account.objects.get(currentUser='True')

    def test_login_4_arguments(self):
        #User enters too many argumants
        self.assertEqual(self.login.login(self.Command5), "Your command is missing arguments.  Please enter your command in the following format: login userName password")

        with self.assertRaises(Account.DoesNotExist):
            A = Account.objects.get(currentUser='True')

    def test_login_2_accounts(self):
        Account.objects.create(userName='Bob', password='wrongPassword', firstName='Bob', currentUser='True')
        #User tries to login when an Account is already logged in
        self.assertEqual(self.login.login(self.Command1), "A user is already logged in")

    def test_logout_success(self):
        Account.objects.create(userName='Bob', password='wrongPassword', firstName='Bob', currentUser='True')
        self.assertEqual(self.login.logout(), "Successfully logged out")

        with self.assertRaises(Account.DoesNotExist):
            A = Account.objects.get(currentUser='True')

    def test_logout_not_logged_in(self):
        #loging out when no Account is the current user

        self.assertEqual(self.login.logout(), "Please log in First")

        with self.assertRaises(Account.DoesNotExist):
            A = Account.objects.get(currentUser='True')
