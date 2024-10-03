from typing import Union
from fastapi import APIRouter
from src.schemas.schemas import Error
from src.schemas.auth import Token
from src.schemas.user import UserCredentials
from src.utils.util import user_exists
from src.services.auth import generate_jwt

router = APIRouter()

@router.post("/token/", response_model=Union[Token, Error])
async def generate_token(user_data: UserCredentials):
    if user_exists(user_data):
        return generate_jwt(user_data)
    else:
        return Error(message=f"User {user_data.username} does not exist")
