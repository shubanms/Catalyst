from src.schemas.schemas import Subjects, Error, Acknowledgement
from src.db.database_loader import DataBaseLoader

database = DataBaseLoader()

def add_subject(username: str, subjects: Subjects):
    all_subjects = database.get_all_subjects().subjects
    
    subjects_to_add = []
    
    for subject in subjects.subjects:
        if subject in all_subjects:
            user_subjects = database.get_user_subjects(username).subjects
            
            if subject in user_subjects:
                continue
            else:
                subjects_to_add.append(subject)
    
    if len(subjects_to_add) > 0:            
        database.add_user_subject(username, subjects_to_add)
        return Acknowledgement(message="Added the subjects!")
    else:
        return Error(message="Can not add subjects!")
