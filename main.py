from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from models import UserModel
from service import UserService
from dao import UserDao

app = FastAPI()

@app.get("/api/test")
def root():
    return "Hellow world"
@app.post("/api/test")
def Is_Successed(request: dict) -> dict: 
    key = request.get('key')
    if key == "cxcxc":
        return {"message": "Succeeded"}
    else:
        return {"message": "Failed"}
    
# Initialize DAO and Service
user_dao = UserDao(filename='users.json')
user_service = UserService(dao=user_dao)

# Request models
class UserCreateRequest(BaseModel):
    name: str
    height: float
    weight: float

# Routes
@app.get("/api/user", response_model=List[UserModel])
def get_all_users():
    return user_service.get_all_users()

@app.post("/api/user", response_model=UserModel)
def create_user(user_request: UserCreateRequest):
    user = UserModel(name=user_request.name, height=user_request.height, weight=user_request.weight)
    user_service.add_user(user)
    return user
