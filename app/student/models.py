from app.common.models import Person
class Student(Person):
    def __init__(self, grade, id, name):
        Person.__init__(self, id, name)
        self.grade = grade
