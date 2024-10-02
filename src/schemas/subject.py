from typing import Optional, List
from pydantic import BaseModel

class Subjects(BaseModel):
    subjects: Optional[List] = []
