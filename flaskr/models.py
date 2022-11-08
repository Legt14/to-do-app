from flask_login import UserMixin
#from werkzeug.security import generate_password_hash, check_password_hash

from .crud import get_users


class User(UserMixin):
    def __init__(self, id, name, email, password, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin


    # def set_password(self, password):
    #     self.password = generate_password_hash(password)


    #def check_password(self, password):
    #    return check_password_hash(self.password, password)

    
    def get_user(username):
        users = get_users()
        for record in users:
            if record.id == username:
                return record
            