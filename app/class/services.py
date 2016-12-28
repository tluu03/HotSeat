import Class
class ClassService():
    def __init__(self, db):
	    self.db = db

    def get_class(self):
	    return 1

    def add_class(self, c):
        c = self.db.add_class()
        return c

    def delete_class(self, c):
        pass

    def edit_class(self, c):
        pass
