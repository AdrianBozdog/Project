from django.test import TestCase
from Course.CreateCourse import CreateCourse
from Course.models import Course
from main import models


class Test_CreateCourse(TestCase):
    def setUp(self):
        self.CC = CreateCourse()

        # Create some courses to test against
        Course.objects.create(name="TemporalMechanics", number=784, onCampus=True,
                              classDays="MW", classHoursStart=1000, classHoursEnd=1100)

        Course.objects.create(name="WarpTheory", number=633, onCampus=False, classDays="TR",
                              classHoursStart=1200, classHoursEnd=1250)

        # Commands to tests that a course can successfully be created
        self.command_create_course = ["createCourse", "NebulaStudies", "432", "Campus", "MW", "1300", "1400"]
        self.command_create_course2 = ["createCourse", "StarshipDesign", "275", "Online", "NN", "0000", "0000"]

        # Command to make sure a course that already exists cannot be created
        self.command_course_already_exists = ["createCourse", "TemporalMechanics", "784", "Campus", "MW",
                                              "1000", "1100"]

        # Commands to test missing command arguments
        self.command_create_course_missing_args1 = ["createCourse", "ReplicatorStudies",
                                                    "809", "Campus", "MW", "2000"]
        self.command_create_course_missing_args2 = ["createCourse", "ReplicatorStudies", "809", "Campus", "MW"]
        self.command_create_course_missing_args3 = ["createCourse", "ReplicatorStudies", "809", "Campus"]
        self.command_create_course_missing_args4 = ["createCourse", "ReplicatorStudies", "809"]
        self.command_create_course_missing_args5 = ["createCourse", "ReplicatorStudies"]
        self.command_create_course_missing_args6 = ["createCourse"]

        # Commands to test invalid course number
        self.command_create_course_invalid_courseNum = ["createCourse", "DilithiumHarvesting", "abc", "Campus",
                                                        "MW", "1300", "1400"]
        self.command_create_course_invalid_courseNum2 = ["createCourse", "DilithiumHarvesting", "12345", "Campus",
                                                         "MW", "1300", "1400"]
        self.command_create_course_invalid_courseNum3 = ["createCourse", "DilithiumHarvesting", "1", "Campus",
                                                         "MW", "1300", "1400"]
        self.command_create_course_invalid_courseNum4 = ["createCourse", "DilithiumHarvesting", "12", "Campus",
                                                         "MW", "1300", "1400"]
        self.command_create_course_invalid_courseNum5 = ["createCourse", "DilithiumHarvesting", "1a2", "Campus",
                                                         "MW", "1300", "1400"]
        # Commands to test invalid location
        self.command_create_course_invalid_location = ["createCourse", "DilithiumHarvesting", "450", "Mars",
                                                         "MW", "1300", "1400"]

        # Commands to test invalid course days
        self.command_create_course_invalid_days = ["createCourse", "InterspeciesEthics", "307", "Online", "q",
                                                   "1200", "1300"]
        self.command_create_course_invalid_days2 = ["createCourse", "InterspeciesEthics", "307", "Online", "123",
                                                   "1200", "1300"]
        self.command_create_course_invalid_days3 = ["createCourse", "InterspeciesEthics", "307", "Online", "My",
                                                   "1200", "1300"]

        # Commands to test invalid times
        self.command_create_course_invalid_time = ["createCourse", "InterspeciesEthics", "207", "Campus", "M",
                                                   "abcd", "1400"]
        self.command_create_course_invalid_time1 = ["createCourse", "InterspeciesEthics", "207", "Campus", "M",
                                                   "1300", "abcd"]
        self.command_create_course_invalid_time2 = ["createCourse", "InterspeciesEthics", "207", "Campus", "M",
                                                   "9000", "1200"]
        self.command_create_course_invalid_time3 = ["createCourse", "InterspeciesEthics", "207", "Campus", "M",
                                                   "1200", "6079"]


    def test_course_successfully_created(self):
        self.assertEqual(CreateCourse.createCourse(self.CC, self.command_create_course), "Course successfully created")
        self.assertEqual(CreateCourse.createCourse(self.CC, self.command_create_course2), "Course successfully created")

        A = Course.objects.get(name="NebulaStudies")
        self.assertEqual(A.name, "NebulaStudies")
        self.assertEqual(A.number, 432)
        self.assertEqual(A.onCampus, True)
        self.assertEqual(A.classDays, "MW")
        self.assertEqual(A.classHoursStart, 1300)
        self.assertEqual(A.classHoursEnd, 1400)

        B = Course.objects.get(name="StarshipDesign")
        self.assertEqual(B.name, "StarshipDesign")
        self.assertEqual(B.number, 275)
        self.assertEqual(B.onCampus, False)
        self.assertEqual(B.classDays, " ")
        self.assertEqual(B.classHoursStart, 0000)
        self.assertEqual(B.classHoursEnd, 0000)


    def test_create_course_already_exists(self):
        self.assertEqual((CreateCourse.createCourse(self.CC, self.command_course_already_exists)),
                         "Course already exists")


    def test_create_course_missing_args(self):
        self.assertEqual((CreateCourse.createCourse(self.CC, self.command_create_course_missing_args1)),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber onCampus daysOfWeek start end")
        self.assertEqual((CreateCourse.createCourse(self.CC, self.command_create_course_missing_args2)),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber onCampus daysOfWeek start end")
        self.assertEqual((CreateCourse.createCourse(self.CC, self.command_create_course_missing_args3)),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber onCampus daysOfWeek start end")
        self.assertEqual((CreateCourse.createCourse(self.CC, self.command_create_course_missing_args4)),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber onCampus daysOfWeek start end")
        self.assertEqual((CreateCourse.createCourse(self.CC, self.command_create_course_missing_args5)),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber onCampus daysOfWeek start end")
        self.assertEqual((CreateCourse.createCourse(self.CC, self.command_create_course_missing_args6)),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber onCampus daysOfWeek start end")

    def test_create_course_invalid_courseNum(self):
        self.assertEqual(CreateCourse.createCourse(self.CC, self.command_create_course_invalid_courseNum),
                         "Course number must be numeric and three digits long")
        self.assertEqual(CreateCourse.createCourse(self.CC, self.command_create_course_invalid_courseNum2),
                         "Course number must be numeric and three digits long")
        self.assertEqual(CreateCourse.createCourse(self.CC, self.command_create_course_invalid_courseNum3),
                         "Course number must be numeric and three digits long")
        self.assertEqual(CreateCourse.createCourse(self.CC, self.command_create_course_invalid_courseNum4),
                         "Course number must be numeric and three digits long")
        self.assertEqual(CreateCourse.createCourse(self.CC, self.command_create_course_invalid_courseNum5),
                         "Course number must be numeric and three digits long")

    def test_invalid_location(self):
        self.assertEqual(CreateCourse.createCourse(self.CC, self.command_create_course_invalid_location),
                         "Location is invalid, please enter campus or online.")

    def test_invalid_days(self):
        self.assertEqual(CreateCourse.createCourse(self.CC, self.command_create_course_invalid_days),
                         "Invalid days of the week, please enter days in the format: MWTRF or NN for online")
        self.assertEqual(CreateCourse.createCourse(self.CC, self.command_create_course_invalid_days2),
                         "Invalid days of the week, please enter days in the format: MWTRF or NN for online")
        self.assertEqual(CreateCourse.createCourse(self.CC, self.command_create_course_invalid_days3),
                         "Invalid days of the week, please enter days in the format: MWTRF or NN for online")

    def test_invalid_times(self):
        self.assertEqual(CreateCourse.createCourse(self.CC, self.command_create_course_invalid_time),
                         "Invalid start or end time, please use a 4 digit military time representation")
        self.assertEqual(CreateCourse.createCourse(self.CC, self.command_create_course_invalid_time1),
                         "Invalid start or end time, please use a 4 digit military time representation")
        self.assertEqual(CreateCourse.createCourse(self.CC, self.command_create_course_invalid_time2),
                         "Invalid start or end time, please use a 4 digit military time representation")
        self.assertEqual(CreateCourse.createCourse(self.CC, self.command_create_course_invalid_time3),
                         "Invalid start or end time, please use a 4 digit military time representation")