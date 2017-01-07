from app.student.models import Student as student

class StudentService():
    # TODO: use Python naming standards
    def __init__(self):
        pass

    def get_students(self):
        return student.query.all()

    def add_student(self, student):
        pass

    def delete_student(self, id):
        pass

    def edit_student(self, student):
        pass
