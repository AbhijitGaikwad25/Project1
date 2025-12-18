# This file is intentionally created to test metadata extraction

from utils.jwt import JWTUtil
from models.user import UserModel
from fastapi import Depends

class AuthService(UserModel):
    def __init__(self):
        pass

    def login(self, username: str, password: str):
        token = JWTUtil.generate_token({"user": username})
        return {"token": token}

def helper_function():
    print("This is a helper function")
    
def another_helper():
    print("This is another helper function")

def another():
    print("This is another helper function")

def helper():
    print("This is another helper function")
