import ClassService
import unittest

# Gut out HotseatTestCase into seperate test case files
# Research how to run all test cases at once
class ClassServiceTestCase(unittest.TestCase):
    def setUp(self):
        db = None
        self.class_service = ClassService.ClassService(db)

    def test_get_class(self):
        answer = 1
        c = self.class_service.get_class()
        self.assertEqual(answer, c)

# if __name__ == '__main__':
#    unittest.main()
