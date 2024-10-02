from fastapi import APIRouter, Depends

from src.schemas.user import NewUser
from src.schemas.subject import Subjects
from src.db.loader.subject import SubjectsDataLoader

from src.services.auth import authenticator
from src.services.register import register_new_user
from src.services.generators import generate_new_quiz


database = SubjectsDataLoader()

router = APIRouter()

@router.post("/register/")
async def register(user: NewUser):
    return register_new_user(user)

# Show all the subjects for new user
@router.get("/show-subjects/")
async def show_all_subjects(username=Depends(authenticator)):
    return database.get_subjects()

# Generate quiz for a new user
@router.get("/generate-quiz/")
async def generate_quiz(quiz_params: Subjects, username=Depends(authenticator)):
    return generate_new_quiz(quiz_params)
