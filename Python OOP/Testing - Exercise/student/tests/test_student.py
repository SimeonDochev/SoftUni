from unittest import TestCase, main
from project.student import Student


class StudentTests(TestCase):
    def setUp(self) -> None:
        self.student = Student("Test", {"python": ['note1', 'note2']})

    def test_student_init(self):
        self.assertEqual("Test", self.student.name)
        self.assertEqual({"python": ['note1', 'note2']}, self.student.courses)

    def test_enroll_existing_course_notes_updated(self):
        self.assertEqual({"python": ['note1', 'note2']}, self.student.courses)
        expected_result = "Course already added. Notes have been updated."
        actual_result = self.student.enroll('python', ['note3'])
        self.assertEqual(expected_result, actual_result)
        self.assertEqual({"python": ['note1', 'note2', 'note3']}, self.student.courses)

    def test_enroll_new_course_with_notes_empty_string(self):
        self.assertEqual({"python": ['note1', 'note2']}, self.student.courses)
        expected_result = "Course and course notes have been added."
        actual_result = self.student.enroll("java", ['note1'])
        self.assertEqual(expected_result, actual_result)
        self.assertEqual({"python": ['note1', 'note2'], "java": ['note1']}, self.student.courses)

    def test_enroll_new_course_with_notes_with_y(self):
        self.assertEqual({"python": ['note1', 'note2']}, self.student.courses)
        expected_result = "Course and course notes have been added."
        actual_result = self.student.enroll("java", ['note1'], "Y")
        self.assertEqual(expected_result, actual_result)
        self.assertEqual({"python": ['note1', 'note2'], "java": ['note1']}, self.student.courses)

    def test_enroll_new_course_without_notes(self):
        self.assertEqual({"python": ['note1', 'note2']}, self.student.courses)
        expected_result = "Course has been added."
        actual_result = self.student.enroll("java", ['note1'], "N")
        self.assertEqual(expected_result, actual_result)
        self.assertEqual({"python": ['note1', 'note2'], "java": []}, self.student.courses)

    def test_add_notes_existing_course(self):
        self.assertEqual({"python": ['note1', 'note2']}, self.student.courses)
        expected_result = "Notes have been updated"
        actual_result = self.student.add_notes("python", 'note3')
        self.assertEqual(expected_result, actual_result)
        self.assertEqual({"python": ['note1', 'note2', 'note3']}, self.student.courses)

    def test_add_notes_non_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("java", 'note3')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual({"python": ['note1', 'note2']}, self.student.courses)

    def test_leave_course_existing_course(self):
        self.assertEqual({"python": ['note1', 'note2']}, self.student.courses)
        expected_result = "Course has been removed"
        actual_result = self.student.leave_course("python")
        self.assertEqual(expected_result, actual_result)
        self.assertEqual({}, self.student.courses)

    def test_leave_course_non_existing_course_raises(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("java")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        self.assertEqual({"python": ['note1', 'note2']}, self.student.courses)


if __name__ == "__main__":
    main()
