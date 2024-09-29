from src.schemas.schemas import NewQuizParams, NewQuiz
from src.models.models import Model

model = Model()


def generate_new_quiz(params: NewQuizParams):
    return model.generate_quiz(params)