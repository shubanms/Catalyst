from typing import Optional
from pydantic import BaseModel

class TopicQuizParams(BaseModel):
    subject: Optional[str] = ""
    topic: Optional[str] = ""
    topic_content: Optional[str] = ""
    number_of_questions: Optional[int] = 10
