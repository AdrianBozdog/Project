from django.test import TestCase
from Account.models import Account
from CurrentUserHelper import CurrentUserHelper


class TestCurrentUserHelper(TestCase):
    def setUp(self):
        self.CUH = CurrentUserHelper()
        Account.objects.create(userName='admin', currentUser='True', title=5)

    def test_isCurrent_true(self):
        self.assertTrue(self.CUH.isCurrent())

    def test_isCurrent_false(self):
        A = Account.objects.get(currentUser='True')
        A.currentUser = False
        A.save()

        self.assertFalse(self.CUH.isCurrent())

    def test_getCurrentUser(self):
        A = Account.objects.get(currentUser='True')

        B = self.CUH.getCurrentUser()

        self.assertEqual(A, B)

    def test_getCurrentUser_None(self):
        A = Account.objects.get(currentUser='True')
        A.currentUser = False
        A.save()

        B = self.CUH.getCurrentUser()

        self.assertIsNone(B)

    def test_getCurrentUserTitle(self):
        self.assertEqual(self.CUH.getCurrentUserTitle(), 5)

    def test_getCurrentUserTile(self):
        A = Account.objects.get(currentUser='True')
        A.currentUser = False
        A.save()

        self.assertEqual(self.CUH.getCurrentUserTitle(), 0)
