from src.schemas.schemas import Error, Acknowledgement
from src.schemas.subject import Subjects
from src.db.loader.subject import SubjectsDataLoader
from src.db.loader.user import UserDataLoader

subjects_database = SubjectsDataLoader()
user_database = UserDataLoader()

def add_subject(username: str, subjects: Subjects):
    all_subjects = subjects_database.get_subjects().subjects
    
    subjects_to_add = []
    
    for subject in subjects.subjects:
        if subject in all_subjects:
            user_subjects = user_database.get_subjects(username)
            
            if subject in user_subjects:
                continue
            else:
                subjects_to_add.append(subject)
    
    if len(subjects_to_add) > 0:            
        user_database.add_subjects(username, subjects_to_add)
        return Acknowledgement(message="Added the subjects!")
    else:
        return Error(message="Subject already added!")

def remove_subject(username: str, subjects: Subjects):
    all_subjects = subjects_database.get_subjects().subjects
    
    subjects_to_remove = []
    
    for subject in subjects.subjects:
        if subject in all_subjects:
            user_subjects = user_database.get_subjects(username)
            
            if subject in user_subjects:
                subjects_to_remove.append(subject)
            else:
                continue
            
    if len(subjects_to_remove) > 0:
        user_database.remove_subjects(username, subjects_to_remove)
        return Acknowledgement(message = "Deleted the subjects!")
    else:
        return Error(message="Could not delete the subjects!")
