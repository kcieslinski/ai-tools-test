from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    age: int

users = []

@app.post("/users/", response_model=User)
def create_user(user: User):
    users.append(user)
    return user

@app.get("/users/", response_model=List[User])
def read_users():
    return users

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "User not found"}

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    for i in range(len(users)):
        if users[i].id == user_id:
            users[i] = user
            return user
    return {"error": "User not found"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i in range(len(users)):
        if users[i].id == user_id:
            del users[i]
            return {"message": "User deleted successfully"}
    return {"error": "User not found"}
