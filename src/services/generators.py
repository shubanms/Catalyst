from src.schemas.quiz import TopicQuizParams
from src.schemas.subject import Subjects
from src.models.models import Model
from src.db.loader.subject import SubjectsDataLoader
from src.utils.util import merge_multiple_quizzes

database = SubjectsDataLoader()
model = Model()


# TODO - Add in validator for subjects
def generate_new_quiz(params: Subjects):
    quizzes = []
    
    data = database.get_random_topics(params.subjects)
    
    for subject, topics in zip(params.subjects, data):
        for topic, _ in topics:
            sample_data = TopicQuizParams(subject=subject, topic=topic, number_of_questions=1)
            quiz = model.generate_quiz(sample_data)
            quizzes.append(quiz)
            
    quiz = merge_multiple_quizzes(quizzes)
    
    return quiz

# TODO - Add in validator to check if topic and topic content exist in the DB
def generate_new_topic_quiz(params: TopicQuizParams):
    return model.generate_topic_quiz(params)
