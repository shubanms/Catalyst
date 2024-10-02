import jwt
import os

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta

from src.schemas.auth import Token
from src.schemas.user import UserCredentials
from src.utils.util import user_exists

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticator(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, os.getenv('JWT_SECRET_KEY'), algorithms=[os.getenv('JWT_ALGORITHM')])
        
        username = payload.get("username")
        password = payload.get("password")
        
        print(username, password)
        
        user_data = UserCredentials(username=username, password=password)
        
        if user_exists(user_data):
            return username
        else:
            raise HTTPException(status_code=403, detail="Invalid credentials")
    except:
        raise HTTPException(status_code=403, detail="Could not validate token")

def generate_jwt(user_data: UserCredentials):
    expire = datetime.now() + timedelta(minutes=30)
    
    data = user_data.model_dump()
    data.update({"exp": expire})
    
    token = jwt.encode(data, os.getenv('JWT_SECRET_KEY'), algorithm=os.getenv('JWT_ALGORITHM'))
    
    jwt_data = Token(username=user_data.username, token=token)
    
    return jwt_data
