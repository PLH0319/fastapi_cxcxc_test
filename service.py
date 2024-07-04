from typing import List
from models import UserModel
from dao import UserDao

class UserService:
    def __init__(self, dao: UserDao):
        self.dao = dao

    def get_all_users(self) -> List[UserModel]:
        return self.dao.get_all_users()

    def add_user(self, user: UserModel):
        users = self.dao.get_all_users()
        users.append(user)
        self.dao.write_users(users)
