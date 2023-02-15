from uuid import UUID
from fastapi import APIRouter
from models.users import User

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

users: list[User] = []


@router.get('', response_model=list[User])
async def get_user() -> list[User]:
    return users


@router.post('')
async def create_user(user: User) -> dict[str, str]:
    users.append(user)
    message: dict[str, str] = {
        'message': 'Success',
    }
    return message


@router.get('/{id}')
async def get_user(id: UUID):
    user = next((user for user in users if user.id == id), None)
    return user
