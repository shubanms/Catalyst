import random

from src.db.connector import DatabaseConnector
from src.db.query.user import UserQueries
from src.schemas.user import User 

DatabaseConnector.initialize()

db_queries = UserQueries(DatabaseConnector)

class UserDataLoader:
    def __init__(self):
        self.db_queries = db_queries
        
    def username_exists(self, username: str):
        return self.db_queries.user_exists(username)
        
    def register_user(self, user: User):
        self.db_queries.add_new_user(user)
        
    def get_id(self, username: str):
        data = self.db_queries.fetch_id(username)
        
        user_id = data[0][0]
        
        return user_id
    
    def get_details(self, username: str):
        user_details = User()
        
        data = self.db_queries.fetch_details(username)
        
        user_details.user_id = data[0][0]
        user_details.name = data[0][1]
        user_details.email = data[0][2]
        user_details.password_hash = data[0][3]
        user_details.username = data[0][4]
        
        return user_details
    
    def get_subjects(self, username: str):
        data = self.db_queries.fetch_subjects

    def get_topic(self, username: str):
        data = self.db_queries.fetch_subjects
