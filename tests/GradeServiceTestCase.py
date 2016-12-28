import unittest
import GradeService

class GradeServiceTestCase(unittest.TestCase):
    def setUp(self):
        db = None
        self.grade_service = GradeService.GradeService(db)

    def test_calculate_average(self):
        db = None
        self.grade_service = GradeService.GradeService(db)

# if __name__ == '__main__':
#    unittest.main()
