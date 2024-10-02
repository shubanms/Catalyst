from src.db.connector import DatabaseConnector

class SubjectQueries:
    def __init__(self, db_connector: DatabaseConnector):
        self.db_connector = db_connector
    
    def fetch_all_subjects(self):
        query = 'SELECT "NAME" FROM "SUBJECTS_TABLE" ORDER BY "SUBJECT_ID";'
        return self.db_connector.execute(query)

    def add_user_subject(self, username: str, subjects: list):
        placeholders = ', '.join(['%s'] * len(subjects))
        query = f'''
            INSERT INTO "USER_SUBJECTS_TABLE" ("USER_ID", "SUBJECT_ID")
            SELECT ut."USER_ID", st."SUBJECT_ID"
            FROM "USERS_TABLE" ut
            JOIN "SUBJECTS_TABLE" st ON st."NAME" IN ({placeholders})
            WHERE ut."USERNAME" = %s;
        '''
        params = (*subjects, username)
        return self.db_connector.execute(query, params, update=True)

    def fetch_random_topics(self, subject: str):
        query = '''
            SELECT "TOPIC_NAME", "TOPIC_CONTENT"
            FROM "TOPIC_TABLE" tt
            WHERE "SUBJECT_ID" IN (
                SELECT "SUBJECT_ID"
                FROM "SUBJECTS_TABLE"
                WHERE "NAME" = %s
            )
            ORDER BY RANDOM()
            LIMIT 5;
        '''
        
        params = (subject,)
        
        return self.db_connector.execute(query=query, params=params)
