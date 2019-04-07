from django.test import TestCase
from Account.models import Account
from Lab.models import Lab
from Course.models import Course
from InstructorCourse.models import InstructorCourse
from TACourse.models import TACourse
from TaLab.models import TaLab
from ViewCourseAssign.models import viewCourseAssign

class TestViewCourseAssign(TestCase):

    def setUp(self):
        self.VCA = viewCourseAssign()
        self.account1 = Account.objects.create(userName='instructor', title='2')
        self.account2 = Account.objects.create(userName='taman', title='1')
        self.account3 = Account.objects.create(userName='joe', title='1')
        self.account4 = Account.objects.create(userName='admin', title='3')
        self.course1 = Course.objects.create(number='361', name='IntroSoftwareEngineering')
        self.course2 = Course.objects.create(number='101', name='English')
        self.course3 = Course.objects.create(name='History', number='101')
        self.lab1 = Lab.objects.create(sectionNumber='801', course=self.course1)
        InstructorCourse.objects.create(Instructor=self.account1, Course=self.course1)
        InstructorCourse.objects.create(Instructor=self.account1, Course=self.course2)
        TACourse.objects.create(TA=self.account2, Course=self.course1)
        TaLab.objects.create(TA=self.account2, Lab=self.lab1)

    def test_viewCourseAssign_accountNotFound(self):
        self.assertEqual(self.VCA.viewCourseAssign(["viewCourseassign", "homer"]), "Account not found")

    def test_viewCourseAssign_admin(self):
        self.assertEqual(self.VCA.viewCourseAssign(["viewCourseassign", "admin"]), "Only Ta and Instructor accounts can have Assignments")

    def test_viewCourseAssign_supervisor(self):
        self.account4.title = 4

        self.assertEqual(self.VCA.viewCourseAssign(["viewCourseassign", "admin"]), "Only Ta and Instructor accounts can have Assignments")

    def test_viewCourseAssign_noAssignments(self):
        self.assertEqual(self.VCA.viewCourseAssign(["viewcourseassign", "joe"]), "joe does not have any assignments")

    def test_viewCourseAssign_Instructor_1Course(self):
        InstructorCourse.objects.get(Instructor=self.account1, Course=self.course2).delete()

        self.assertEqual(self.VCA.viewCourseAssign(["viewcourseassign", "instructor"]), "instructor is assigned to: IntroSoftwareEngineering")

    def test_viewCourseAssign_Instructor_2Course(self):

        self.assertEqual(self.VCA.viewCourseAssign(["viewcourseassign", "instructor"]), "instructor is assigned to: IntroSoftwareEngineering, English")

    def test_viewCourseAssign_TA_CourseLab(self):

        self.assertEqual(self.VCA.viewCourseAssign(["viewcourseassign", "taman"]), "taman is assigned to: IntroSoftwareEngineering section 801")

    def test_viewCourseAssign_Ta_2CourseLab(self):
        self.lab2 = Lab.objects.create(sectionNumber='801', course=self.course2)
        TaLab.objects.create(TA=self.account2, Lab=self.lab2)

        self.assertEqual(self.VCA.viewCourseAssign(["viewcourseassign", "taman"]),
                         "taman is assigned to: IntroSoftwareEngineering section 801, English section 801")

    def test_viewCourseAssign_Ta_2CourseLab_1Course(self):
        self.lab2 = Lab.objects.create(sectionNumber='801', course=self.course2)
        TaLab.objects.create(TA=self.account2, Lab=self.lab2)
        TACourse.objects.create(TA=self.account2, Course=self.course3)

        self.assertEqual(self.VCA.viewCourseAssign(["viewcourseassign", "taman"]),
                         "taman is assigned to: IntroSoftwareEngineering section 801, English section 801, History")

    def test_viewCourseAssign_TA_noLabs(self):
        TaLab.objects.get(TA=self.account2).delete()

        self.assertEqual(self.VCA.viewCourseAssign([" ", "taman"]), "taman is assigned to: IntroSoftwareEngineering")

    def test_viewCourseAssign_Ta_1CourseLab_1Course(self):
        TACourse.objects.create(TA=self.account2, Course=self.course2)

        self.assertEqual(self.VCA.viewCourseAssign([" ", "taman"]), "taman is assigned to: IntroSoftwareEngineering section 801, English")
