from django.test import TestCase
from InstructorCourse.assignInst import assignInst
from InstructorCourse.models import InstructorCourse
from Course.models import Course
from Account.models import Account


class TestAssignInst(TestCase):

    def setUp(self):
        self.account1 = Account.objects.create(userName="cheng41", title="2")
        self.course1 = Course.objects.create(number="535", name="AlgorithmDesignAndAnalysis")
        self.course2 = Course.objects.create(number="317")
        self.AI = assignInst()

    def test_assignInst_successfully_created(self):

        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "cheng41", "535"]),
                         "Instructor was successfully assigned to class")
        self.assertTrue(InstructorCourse.objects.exists())
        A = Account.objects.get(userName="cheng41")
        B = Course.objects.get(number="535")

        self.assertEqual(A.userName, "cheng41")
        self.assertEqual(B.number, 535)

    def test_assignInt_already_exists(self):
        InstructorCourse.objects.create(Instructor=self.account1, Course=self.course1)

        self.assertEqual(self.AI.assignInst(["", "cheng41", "535"]), "This class was already assigned")

    def test_assignInst_no_argument(self):
        self.assertEqual(self.AI.assignInst(["assigninstructorcourse"]),
                         "Your argument is missing commands, please enter your command in the following format: " \
                         "assigninstructorcourse userName courseNumber")

    def test_assignInst_no_argument_courseNumber(self):
        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "bob824"]),
                         "Your argument is missing commands, please enter your command in the following format: " \
                         "assigninstructorcourse userName courseNumber")

    def test_assignInst_no_argument_username(self):
        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "250"]),
                         "Your argument is missing commands, please enter your command in the following format: " \
                         "assigninstructorcourse userName courseNumber")

    def test_assignInst_no_courseNumber_found(self):
        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "cheng41", "250"]),
                         "Invalid course number")

    def test_assignInst_no_username_found(self):
        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "bob824", "535"]),
                         "Invalid user name")






