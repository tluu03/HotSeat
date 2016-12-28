import StudentService
import unittest

class StudentServiceTestCase(unittest.TestCase):
    def setUp(self):
        db = None
        self.student_service = StudentService.StudentService(db)

    def test_get_students(self):
        answer = 1
        students = self.student_service.get_students()
        self.assertEqual(answer, students)

if __name__ == '__main__':
    unittest.main()
