import hashlib

from src.schemas.user import UserCredentials
from src.db.loader.user import UserDataLoader

database = UserDataLoader()

def hash_password(password: str):
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    return password_hash


def user_exists(user_data: UserCredentials):
    user_details = database.get_details(user_data.username)
    
    hashed_password = hash_password(user_data.password)
    
    if user_details and user_details.password_hash == hashed_password:
        return True
    else:
        return False

def merge_multiple_quizzes(quiz_list):
    final_quiz = {
        'subject_name': [],
        'questions': [],
        'answer': [],
        'options': []
    }

    for quiz in quiz_list:
        final_quiz['subject_name'] = list(set(final_quiz['subject_name'] + quiz['subject_name']))
        
        final_quiz['questions'] += quiz['questions']
        
        final_quiz['answer'] += quiz['answer']
        
        for opt_list in quiz['options']:
            final_quiz['options'] += opt_list

    return final_quiz
