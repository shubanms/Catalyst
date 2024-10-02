from src.db.connector import DatabaseConnector

class TopicQueries:
    def __init__(self, db_connector: DatabaseConnector):
        self.db_connector = db_connector
    
    def fetch_all_topics(self):
        query = '''
            SELECT s."NAME" AS subject_name, t."TOPIC_NAME" AS topic_name
            FROM "SUBJECTS_TABLE" s
            JOIN "TOPIC_TABLE" t ON s."SUBJECT_ID" = t."SUBJECT_ID";
        '''
        return self.db_connector.execute(query)
    
    def fetch_topics_for_subject(self, subject_name: str):
        query = '''
            SELECT t."TOPIC_NAME"
            FROM "TOPIC_TABLE" t
            JOIN "SUBJECTS_TABLE" s ON t."SUBJECT_ID" = s."SUBJECT_ID"
            WHERE s."NAME" = %s;
        '''
        params = (subject_name,)
        return self.db_connector.execute(query, params)
    
    def fetch_random_topics_for_subject(self, subject: str):
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
        return self.db_connector.execute(query, params)
