from fastapi import APIRouter, Depends

from src.services.auth import authenticator
from src.services.updater import add_subject, remove_subject
from src.services.generators import generate_new_topic_quiz

from src.schemas.subject import Subjects
from src.schemas.quiz import TopicQuizParams
from src.db.loader.user import UserDataLoader


router = APIRouter()
database = UserDataLoader()

# Show subjects for a particular user
@router.get("/show-my-subjects/")
async def show_my_subjects(username = Depends(authenticator)):
    return database.get_subjects(username)

# Show all subjects and topics for a particular user
@router.get("/show-my-topics/")
async def show_my_topics(username = Depends(authenticator)):
    return database.get_topic(username)

# Adds a new subject for some user
@router.post("/add-new-subject/")
async def add_new_subject(subjects: Subjects, username = Depends(authenticator)):
    return add_subject(username, subjects)

@router.post("/delete-subject/")
async def delete_subject(subjects: Subjects, username = Depends(authenticator)):
    return remove_subject(username, subjects)

# Generates a topic related quiz for some user
@router.post("/generate-topic-quiz/")
async def generate_topic_quiz(topic: TopicQuizParams, username = Depends(authenticator)):
    return generate_new_topic_quiz(topic)
