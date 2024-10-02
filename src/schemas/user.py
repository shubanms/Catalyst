from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserCredentials(BaseModel):
    username: Optional[str] = ""
    password: Optional[str] = ""
    
class User(BaseModel):
    user_id: Optional[int] = None
    name: Optional[str] = ""
    email: Optional[EmailStr] = Field(default=None)
    username: Optional[str] = ""
    password_hash: Optional[str] = ""

class NewUser(BaseModel):
    name: str = ""
    username: str = ""
    password: str = ""
    email: EmailStr = ""
