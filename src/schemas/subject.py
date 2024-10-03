from typing import Optional, List
from pydantic import BaseModel

class Subjects(BaseModel):
    subjects: Optional[List] = []

class Topics(BaseModel):
    subject_name: Optional[str]= ""
    topics: Optional[List] = []
