from src.db.connector import DatabaseConnector


class DatabaseQueries:
    def __init__(self, db_connector: DatabaseConnector):
        self.db_connector: DatabaseConnector = db_connector
        
    def _execute_query(self, query: str, params = None):
        """A helper method to execute a SQL query and return results."""
        conn = self.db_connector.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        finally:
            self.db_connector.return_connection(conn)
            
    def fetch_user_id(self, username):
        """
            Fetch the user id for a particular username
        """
        
        query = 'select "USER_ID" from "USERS_TABLE" where "USERNAME" = %s;'
        params = (username,)
        
        return self._execute_query(query, params)

    def fetch_all_subjects(self):
        """
            Fetch all subject names from the subjects table
        """
        
        query = 'SELECT "NAME" FROM "SUBJECTS_TABLE" order by "SUBJECT_ID";'
        
        return self._execute_query(query)
    
    def fetch_all_user_subjects(self, username):
        """
            Fetch all the subjects for a particular user
        """
        
        query = '''
                SELECT st."NAME"
                FROM "SUBJECTS_TABLE" st
                JOIN "USER_SUBJECTS_TABLE" ust ON st."SUBJECT_ID" = ust."SUBJECT_ID"
                JOIN "USERS_TABLE" ut ON ust."USER_ID" = ut."USER_ID"
                WHERE ut."USERNAME" = %s;
                '''
                
        params = (username,)
        
        return self._execute_query(query, params)
    
    def fetch_all_topics(self):
        """
            Fetch all topics
        """
        
        query = '''
                SELECT s."NAME" AS subject_name,
                t."TOPIC_NAME" AS topic_name 
                
                FROM "SUBJECTS_TABLE" s 
                
                JOIN "TOPIC_TABLE" t 
                ON s."SUBJECT_ID" = t."SUBJECT_ID";
                '''
                
        return self._execute_query(query)
            
    def fetch_all_topics_for_subject(self, subject_name: str):
        """
            Fetch all topics for a particular subject ID
        """

        query = '''
                SELECT t."TOPIC_NAME"
                FROM "TOPIC_TABLE" t
                JOIN "SUBJECTS_TABLE" s ON t."SUBJECT_ID" = s."SUBJECT_ID"
                WHERE s."NAME" = %s;
                '''
                
        params = (subject_name,)
        
        return self._execute_query(query, params)
    
    def fetch_user_details(self, username: str):
        """
            Fetch user details from users table based on username
        """
        
        query = 'SELECT "USER_ID", "NAME", "EMAIL", "PASSWORD_HASH", "USERNAME" FROM "USERS_TABLE" where "USERNAME" = %s;'
        params = (username,)
        
        return self._execute_query(query, params)

    def fetch_topics_for_user(self, username: str):
        """
            Fetch the topics for a particular user
        """
        
        query = '''
                SELECT 
                    s."NAME" AS subject_name,
                    t."TOPIC_NAME"
                FROM 
                    "USERS_TABLE" u
                JOIN 
                    "USER_SUBJECTS_TABLE" us ON u."USER_ID" = us."USER_ID"
                JOIN 
                    "SUBJECTS_TABLE" s ON us."SUBJECT_ID" = s."SUBJECT_ID"
                JOIN 
                    "TOPIC_TABLE" t ON s."SUBJECT_ID" = t."SUBJECT_ID"
                WHERE 
                    u."USERNAME" = %s;
                '''
        params = (username,)
        
        return self._execute_query(query, params)

    