from src.db.connector import DatabaseConnector
from src.db.queries import DatabaseQueries

from src.schemas.schemas import DBUser, Subjects

DatabaseConnector.initialize()

db_queries = DatabaseQueries(DatabaseConnector)

class DataBaseLoader:
    def __init__(self):
        self.db_queries = db_queries
        
    def get_user_id(self, username):
        """
            Gets the user id for a particular user
        """
        data = self.db_queries.fetch_user_id(username)
        
        user_id = data[0][0]
        
        return user_id

    def get_all_subjects(self):
        """
            Gets all subjects available on the app
        """
        data = self.db_queries.fetch_all_subjects()
        
        subjects = Subjects(subjects=[item[0].strip() for item in data])
        
        return subjects
    
    def get_user_subjects(self, username):
        """
            Gets all the subjects for a particular user
        """
        
        data = self.db_queries.fetch_all_user_subjects(username)
        
        subjects = Subjects(subjects=[item[0].strip() for item in data])
        
        return subjects
    
    def get_all_topics(self):
        """
            Gets all the topics for each subject in the form of a dictionary key: subject and value: subject-topics
        """
        data = self.db_queries.fetch_all_topics()
        
        topics = {}
        
        for item in data:
            subject = item[0].strip()
            if subject in topics:
                topics[subject].append(item[1].strip())
            else:
                topics[subject] = [item[1].strip()]
        
        return topics
    
    def get_all_topics_for_subject(self, subject_name):
        """
            Gets all the topics for a particular subject name
        """
        
        data = self.db_queries.fetch_all_topics_for_subject(subject_name)
        
        topics = {}
        
        topics[subject_name] = [item[0].strip() for item in data]
        
        return topics
    
    def get_user_details(self, username: str) -> DBUser:
        user_details = DBUser()
        
        user_data = self.db_queries.fetch_user_details(username)
        
        user_details.user_id = user_data[0][0]
        user_details.name = user_data[0][1]
        user_details.email = user_data[0][2]
        user_details.password_hash = user_data[0][3]
        user_details.username = user_data[0][4]
        
        return user_details
    
    def get_user_topics(self, username):
        """
            Gets all the topics for a particular user
        """
        
        data = self.db_queries.fetch_topics_for_user(username)
        
        topics = {}
        
        for item in data:
            subject = item[0].strip()
            
            if subject in topics:
                topics[subject].append(item[1].strip())
            else:
                topics[subject] = [item[1].strip()]
        
        return topics