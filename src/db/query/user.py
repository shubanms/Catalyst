from src.db.connector import DatabaseConnector
from src.schemas.user import NewUser

class UserQueries:
    def __init__(self, db_connector: DatabaseConnector):
        self.db_connector: DatabaseConnector = db_connector
        
    def user_exists(self, username: str):
        query = '''
            SELECT 1
            FROM public."USERS_TABLE"
            WHERE "USERNAME" = %s
            LIMIT 1;
        '''
        params = (username,)
    
        result = self.db_connector.execute(query=query, params=params)
        
        return len(result) > 0
        
    def add_new_user(self, user: NewUser):
        query = '''
            INSERT INTO public."USERS_TABLE"
            ("NAME", "EMAIL", "PASSWORD_HASH", "USERNAME")
            VALUES(%s, %s, %s, %s);
        '''
        
        params = (user.name, user.email, user.password, user.username)
        
        return self.db_connector.execute(query=query, params=params, update=True)
        
    def fetch_id(self, username: str):
        query = 'SELECT "USER_ID" FROM "USERS_TABLE" WHERE "USERNAME" = %s;'
        params = (username,)
        return self.db_connector.execute(query, params)
    
    def fetch_details(self, username: str):
        query = '''
            SELECT "USER_ID", "NAME", "EMAIL", "PASSWORD_HASH", "USERNAME" 
            FROM "USERS_TABLE" 
            WHERE "USERNAME" = %s;
        '''
        params = (username,)
        return self.db_connector.execute(query, params)

    def fetch_subjects(self, username: str):
        query = '''
            SELECT st."NAME"
            FROM "SUBJECTS_TABLE" st
            JOIN "USER_SUBJECTS_TABLE" ust ON st."SUBJECT_ID" = ust."SUBJECT_ID"
            JOIN "USERS_TABLE" ut ON ust."USER_ID" = ut."USER_ID"
            WHERE ut."USERNAME" = %s;
        '''
        params = (username,)
        return self.db_connector.execute(query, params)

    def fetch_topics(self, username: str):
        query = '''
            
        '''