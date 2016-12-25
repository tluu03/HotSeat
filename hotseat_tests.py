import json
# import api
import unittest
import tempfile
import StudentService

class HotseatTestCase(unittest.TestCase):

    def setUp(self):
        # api.app.config['TESTING'] = True
        # self.app = api.app.test_client()
        db = None
        self.student_service = StudentService.StudentService(db)

    def load_json(self, data):
        return json.loads(str(data, 'utf-8'))

    def test_get_index(self):
        pass
    #    out = self.app.get('/')
    #    assert b'data-section="app"' in out.data

    def test_get_students(self):
        # Arrange
        answer = 1

        # Act
        students = self.student_service.get_students()

        # Assert
        self.assertEqual(answer, students)


if __name__ == '__main__':
    unittest.main()
