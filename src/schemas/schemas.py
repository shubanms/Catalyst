from typing import Optional
from pydantic import BaseModel

class Error(BaseModel):
    message: Optional[str] = ""
    
class Acknowledgement(BaseModel):
    message: Optional[str] = ""
