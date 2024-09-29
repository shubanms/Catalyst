from typing import Union

from fastapi import FastAPI, Depends

from src.services.auth import authenticator
from src.db.database_loader import DataBaseLoader
from src.schemas.schemas import User, Error, Token, NewQuizParams, Subjects
from src.utils.util import user_exists
from src.services.auth import generate_jwt, authenticator
from src.db.database_loader import DataBaseLoader
from src.services.generators import generate_new_quiz
from src.services.updater import add_subject

app = FastAPI()
database = DataBaseLoader()

@app.post('/')
def health_check():
    return {'message': 'Server is running!'}

# Generate the JWT for user
@app.get("/token/", response_model=Union[Token, Error])
async def generate_token(user_data: User):
    if user_exists(user_data):
        return generate_jwt(user_data)
    else:
        return Error(message=f"User {user_data.username} does not exist")

# Show all the subjects for new user
@app.get("/show-all-subjects/")
async def show_all_subjects(username = Depends(authenticator)):
    return database.get_all_subjects()

# Generate quiz for a new user
@app.get("/generate-quiz/")
async def generate_quiz(quiz_params: NewQuizParams, username = Depends(authenticator)):
    return generate_new_quiz(quiz_params)

# Show subjects for a particular user
@app.get("/show-my-subjects/")
async def show_my_subjects(username = Depends(authenticator)):
    return database.get_user_subjects(username)

# Show all subjects and topics for a particular user
@app.get("/show-my-topics/")
async def show_my_topics(username = Depends(authenticator)):
    return database.get_user_topics(username)

@app.post("/add-new-subject/")
async def add_new_subject(subjects: Subjects, username = Depends(authenticator)):
    return add_subject(username, subjects)
