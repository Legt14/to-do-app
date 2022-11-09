from flask_login import UserMixin
#from werkzeug.security import generate_password_hash, check_password_hash

from .crud import get_user

class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserModel(UserMixin):
    def __init__(self, user_data):
        """
        :param  user_data: UserData
        """
        self.id = user_data.username
        self.password = user_data.password


    @staticmethod
    def query(user_id):
        user_doc = get_user(user_id)
        user_data = UserData(
            username=user_doc.id,
            password=user_doc.to_dict()['password'])

        return UserModel(user_data)


    # def set_password(self, password):
    #     self.password = generate_password_hash(password)


    #def check_password(self, password):
    #    return check_password_hash(self.password, password)
            