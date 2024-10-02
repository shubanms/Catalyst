from src.schemas.subject import Subjects
from src.db.query.subject import SubjectQueries
from src.db.connector import DatabaseConnector

DatabaseConnector.initialize()

db_queries = SubjectQueries(DatabaseConnector)

class SubjectsDataLoader:
    def __init__(self):
        self.db_queries = db_queries
        
    def get_subjects(self):
        data = self.db_queries.fetch_all_subjects()
        
        subjects = Subjects(subjects=[item[0].strip() for item in data])
        
        return subjects

    def get_random_topics(self, subject: str):
        data = self.db_queries.fetch_random_topics(subject)
        
        return data
