from typing import Union
from fastapi import APIRouter, Depends
from src.services.updater import add_subject
from src.schemas.schemas import Subjects, TopicQuizParams
from src.db.database_loader import DataBaseLoader
from src.services.auth import authenticator
from src.services.generators import generate_new_topic_quiz

router = APIRouter()
database = DataBaseLoader()

# Show subjects for a particular user
@router.get("/show-my-subjects/")
async def show_my_subjects(username = Depends(authenticator)):
    return database.get_user_subjects(username)

# Show all subjects and topics for a particular user
@router.get("/show-my-topics/")
async def show_my_topics(username = Depends(authenticator)):
    return database.get_user_topics(username)

# Adds a new subject for some user
@router.post("/add-new-subject/")
async def add_new_subject(subjects: Subjects, username = Depends(authenticator)):
    return add_subject(username, subjects)

# Generates a topic related quiz for some user
@router.get("/generate-topic-quiz/")
async def generate_topic_quiz(topic: TopicQuizParams, username = Depends(authenticator)):
    return generate_new_topic_quiz(topic)
