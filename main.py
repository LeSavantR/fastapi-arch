from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    email: str
    is_active: bool


app = FastAPI()

users: list[User] = [
    {
        'email': 'rh@mail.io',
        'is_active': True
    },
    {
        'email': 'lm@mail.io',
        'is_active': True
    },
    {
        'email': 'rp@mail.io',
        'is_active': True
    },
    {
        'email': 'em@mail.io',
        'is_active': True
    },
]


@app.get('/users')
async def get_user():
    return users


@app.post('/users')
async def create_user(user: User):
    users.append(user)
    message =  {
        'message': 'Success',
        **user
    }
    return message
