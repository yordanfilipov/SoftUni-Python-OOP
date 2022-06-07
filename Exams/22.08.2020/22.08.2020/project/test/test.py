from project.student_report_card import StudentReportCard

from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def setUp(self):
        self.student = StudentReportCard("Ivan", 10)

    def test_init(self):
        self.assertEqual("Ivan", self.student.student_name)
        self.assertEqual(10, self.student.school_year)
        self.assertEqual({}, self.student.grades_by_subject)

    def test_set_student_name_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_name = ''
        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_set_student_year_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.student.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_add_grade_if_subject_in_list(self):
        self.student.grades_by_subject = {"Math": [5]}
        self.student.add_grade("English", 3)
        self.assertEqual({"Math": [5], "English": [3]}, self.student.grades_by_subject)

    def test_add_grade_if_subject_not_in_list(self):
        self.student.grades_by_subject = {"Math": [5]}
        self.student.add_grade("Math", 3)
        self.assertEqual({"Math": [5, 3]}, self.student.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.student.grades_by_subject = {"Math": [5, 5], "English": [2, 3, 5]}
        result = "Math: 5.00\nEnglish: 3.33"
        self.assertEqual(result, self.student.average_grade_by_subject())

    def test_average_grade_for_all_subjects(self):
        self.student.grades_by_subject = {"Math": [5, 5], "English": [2, 3, 5]}
        result = "Average Grade: 4.00"
        self.assertEqual(result, self.student.average_grade_for_all_subjects())

    def test_repr(self):
        self.student.grades_by_subject = {"Math": [5, 5], "English": [2, 3, 5]}
        result = f"Name: {self.student.student_name}\n" \
                 f"Year: {self.student.school_year}\n" \
                 f"----------\n" \
                 f"{self.student.average_grade_by_subject()}\n" \
                 f"----------\n" \
                 f"{self.student.average_grade_for_all_subjects()}"
        self.assertEqual(result, self.student.__repr__())


if __name__ == '__main__':
    main()
