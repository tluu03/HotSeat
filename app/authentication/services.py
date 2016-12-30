from app.authentication.models import User as user

class UserService():
    def __init__(self):
        pass

    def get_user(self, email):
        return user.query.filter_by(email=email).first()

