from django.test import TestCase
from InstructorCourse.assignInst import assignInst
from InstructorCourse.models import InstructorCourse
from Course.models import Course
from Account.models import Account


class TestAssignInst(TestCase):

    def setUp(self):
        self.account1 = Account.objects.create(userName="cheng41", title="2")
        self.course1 = Course.objects.create(number="535", name="AlgorithmDesignAndAnalysis")
        self.account2 = Account.objects.create(userName="suzuki15", title="2")
        self.course2 = Course.objects.create(number="317", name="DiscreteInformationStructures")
        self.account3 = Account.objects.create(userName="ImNotInstructor", title="1")
        self.account4 = Account.objects.create(userName="ImNotInstructor2", title="3")
        self.AI = assignInst()

    def test_assignInst_successfully_created(self):

        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "cheng41", "535"]),
                         "Instructor was successfully assigned to class")
        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "suzuki15", "317"]),
                         "Instructor was successfully assigned to class")
        self.assertTrue(InstructorCourse.objects.exists())
        a = Account.objects.get(userName="cheng41")
        b = Course.objects.get(number="535")
        c = Account.objects.get(userName="suzuki15")
        d = Course.objects.get(number="317")
        self.assertEqual(a.userName, "cheng41")
        self.assertEqual(b.number, 535)
        self.assertEqual(c.userName, "suzuki15")
        self.assertEqual(d.number, 317)

    def test_assignInt_already_exists(self):
        InstructorCourse.objects.create(Instructor=self.account1, Course=self.course1)
        self.assertEqual(self.AI.assignInst(["", "cheng41", "535"]), "This class is already assigned")
        InstructorCourse.objects.create(Instructor=self.account2, Course=self.course2)
        self.assertEqual(self.AI.assignInst(["", "suzuki15", "317"]), "This class is already assigned")

    def test_assignInst_no_argument(self):
        self.assertEqual(self.AI.assignInst(["assigninstructorcourse"]),
                         "There are arguments missing, Please enter your command in the following format: " \
                         "assigninstructorcourse userName courseNumber")

    def test_assignInst_no_argument_courseNumber(self):
        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "bob824"]),
                         "There are arguments missing, Please enter your command in the following format: " \
                         "assigninstructorcourse userName courseNumber")

    def test_assignInst_no_argument_username(self):
        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "250"]),
                         "There are arguments missing, Please enter your command in the following format: " \
                         "assigninstructorcourse userName courseNumber")

    def test_assignInst_no_courseNumber_found(self):
        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "cheng41", "316"]),
                         "Invalid course number")
        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "suzuki15", "119"]),
                         "Invalid course number")

    def test_assignInst_no_username_found(self):
        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "bob824", "535"]),
                         "Invalid user name")
        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "imTa", "317"]),
                         "Invalid user name")

    def test_assignInt_is_not_instructor(self):
        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "ImNotInstructor", "535"]),
                         "Account is not an instructor")
        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "ImNotInstructor2", "317"]),
                         "Account is not an instructor")






