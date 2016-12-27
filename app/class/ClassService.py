import Class
class ClassService():
    def __init__(self, db):
	    self.db = db

    def get_class(self):
	    return 1

    def add_class(self, class):
        class = self.db.get_class()

        return class

    def delete_class(self, class):
        pass

    def edit_class(self, class):
        pass
