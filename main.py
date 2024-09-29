from typing import Union

from fastapi import FastAPI, Depends

from src.services.auth import authenticator
from src.db.database_loader import DataBaseLoader
from src.schemas.schemas import User, InvalidUser, Token, NewQuizParams, NewQuiz
from src.utils.util import user_exists
from src.services.auth import generate_jwt, authenticator
from src.db.database_loader import DataBaseLoader
from src.services.generators import generate_new_quiz

app = FastAPI()
database = DataBaseLoader()

@app.post('/')
def health_check():
    return {'message': 'Server is running!'}

# Generate the JWT for user
@app.post("/token/", response_model=Union[Token, InvalidUser])
async def generate_token(user_data: User):
    if user_exists(user_data):
        return generate_jwt(user_data)
    else:
        return InvalidUser(message=f"User {user_data.username} does not exist")

# Show all the subjects for new user
@app.post("/show-all-subjects/")
async def show_all_subjects(username = Depends(authenticator)):
    return database.get_all_subjects()

# Generate quiz for a new user
@app.post("/generate-quiz/")
async def generate_quiz(quiz_params: NewQuizParams, username = Depends(authenticator)):
    return generate_new_quiz(quiz_params)

# Show subjects for a particular user
@app.post("/show-my-subjects/")
async def show_my_subjects(username = Depends(authenticator)):
    return database.get_user_subjects(username)

# Show all subjects and topics for a particular user
@app.post("/show-my-topics/")
async def show_my_topics(username = Depends(authenticator)):
    return database.get_user_topics(username)
