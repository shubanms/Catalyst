from typing import Optional, List, Dict
from pydantic import BaseModel
from pydantic import EmailStr, Field
import typing_extensions as typing


class User(BaseModel):
    username: Optional[str] = ""
    password: Optional[str] = ""


class Token(BaseModel):
    username: Optional[str] = ""
    token: Optional[str] = ""


class DBUser(BaseModel):
    user_id: Optional[int] = None
    name: Optional[str] = ""
    email: Optional[EmailStr] = Field(default=None)
    username: Optional[str] = ""
    password_hash: Optional[str] = ""

class Error(BaseModel):
    message: Optional[str] = ""
    
class Acknowledgement(BaseModel):
    message: Optional[str] = ""

class Subjects(BaseModel):
    subjects: Optional[List] = []

class NewQuiz(BaseModel):
    subject_name: Optional[str] = ""
    questions: List[str] = Field(default=[], description="List of questions for the quiz")
    options: List[List[str]] = Field(default=[], description="List of options for each question")
    answer: List[int] = Field(default=[], description="List of correct answer indices")

class NewQuizParams(BaseModel):
    subjects: List[str] = Field(..., description="List of subjects for the quiz")
    rating: List[int] = Field(..., description="List of difficulty ratings for each subject")
