import json
import unittest
import tempfile
import StudentService
import GradeService
import Class
import ClassService
class HotseatTestCase(unittest.TestCase):

    def setUp(self):
        # api.app.config['TESTING'] = True
        # self.app = api.app.test_client()
        db = None
