import json
from typing import List, Dict
from models import UserModel

class UserDao:
    def __init__(self, filename: str):
        self.filename = filename

    def get_all_users(self) -> List[UserModel]:
        with open(self.filename, 'r') as file:
            data = json.load(file)
            users = [UserModel(**user) for user in data]
            return users

    def write_users(self, users: List[UserModel]):
        data = [user.model_dump() for user in users]
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
