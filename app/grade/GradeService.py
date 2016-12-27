import Grade

class GradeService():
    # TODO: use Python naming standards
    def __init__(self, db):
	    self.db = db

    def get_grade(self, grade):
	    return 1

    def add_grade(self, grade):

        pass

    def delete_grade(self, id):
        pass

    def edit_grade(self, grade):
        pass

    def calculate_grade(self, id):
        grades = get_grade(student_id)
        overall = None
        for g in grades:
            score = g.score * g.weight
            overall += score
