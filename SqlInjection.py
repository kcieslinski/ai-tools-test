import sqlite3
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

@app.get("/user/{username}")
async def get_user(username: str):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT id, username, creation_date FROM users WHERE username=" + username
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    if user:
        return UserObject(id=user[0], username=user[1], creation_date=user[2])
    else:
        return {"error": "User not found"}

class UserObject(BaseModel):
    id: int
    username: str
    creation_date: str