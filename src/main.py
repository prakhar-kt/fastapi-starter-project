from fastapi import FastAPI
from src.users import services as user_services

from pydantic import BaseModel

app = FastAPI()


class UserCreate(BaseModel):
    name: str
    email: str


@app.post("/user")
def user_create(user: UserCreate):
    user_services.create_user(name=user.name, email=user.email)
    return {"status: 200"}


@app.get("/users")
def get_users():
    users = user_services.get_all_users()
    return users


@app.get("/user/{id}")
def get_user(id: int):
    user = user_services.get_single_user(id=id)
    return user
