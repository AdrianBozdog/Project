from django.test import TestCase
from InstructorCourse.assignInst import assignInst
from InstructorCourse.models import InstructorCourse
from main import models
from Course.models import Course
from Account.models import Account


class TestAssignInst(TestCase):

    def setUp(self):
        Account.objects.create(userName="cheng41", title="2")
        Course.objects.create(number="535")
        Course.objects.create(number="317")
        self.course1 = Course.objects.get(number="535")
        self.course2 = Course.objects.get(number="317")
        self.AI = assignInst()

    def test_assignInst_successfully_created(self):

        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "cheng41", "535"]),
                         "Instructor was successfully assigned to class")
        self.assertTrue(InstructorCourse.objects.exists())
        a=InstructorCourse.objects.get()
        self.assertEqual(a.course, Course.objects.get(number="535"))
        self.assertEqual(a.course, Course.objects.get(number="317"))
        self.assertEqual(a.instructor, Account.objects.get(userName="cheng41"))

    def test_assignInst_no_argument(self):
        self.assertEqual((self.AI.assignInst(["assigninstructorcourse"])),
                         "Please, type the command in the following format assigninstructorcourse classNumber username")

    def test_assignInst_no_argument_courseNumber(self):
        self.assertEqual((self.AI.assignInst(["assigninstructorcourse", "bob824"])),
                         "Please, type the command in the following format assigninstructorcourse classNumber username")

    def test_assignInst_no_argument_username(self):
        self.assertEqual((self.AI.assignInst(["assigninstructorcourse","250"])),
                         "Please, type the command in the following format assigninstructorcourse classNumber username")

    def test_assignInst_no_courseNumber_found(self):
        self.assertEqual((self.AI.assignInst(["assigninstructorcourse", "bob824" "250"])),
                         "Invalid course number")

    def test_assignInst_no_username_found(self):
        self.assertEqual((self.AI.assignInst(["assigninstructorcourse", "magul" "595"])),
                         "Invalid account name")


