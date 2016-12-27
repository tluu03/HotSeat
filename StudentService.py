import Student

class StudentService():
    # TODO: use Python naming standards
    def __init__(self, db):
	    self.db = db

    def get_students(self):
	    return 1

    def add_student(self, student):
        students = self.db.get_students()

        return students

    def delete_student(self, id):
        pass

    def edit_student(self, student):
        pass
