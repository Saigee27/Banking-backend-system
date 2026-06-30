from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []

class UserCreate(BaseModel):
    name: str
    email: str

@app.get("/")
def home():
    return {
        "message": "Banking Backend is Alive"
    }

@app.get("/users")
def get_users():
    return users

@app.post("/users")
def create_user(user: UserCreate):
    new_user = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email
    }

    users.append(new_user)

    return {
        "message": "User created successfully",
        "user": new_user
    }