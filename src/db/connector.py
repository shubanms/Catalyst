import os

from dotenv import load_dotenv
from psycopg2 import pool

load_dotenv()

class DatabaseConnector:
    _connection_pool = None

    @classmethod
    def initialize(cls):
        """Initialize the connection pool"""
        cls._connection_pool = pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
            port=5432,
            database=os.getenv('DB_NAME')
        )

    @classmethod
    def get_connection(cls):
        """Fetch a connection from the pool"""
        if cls._connection_pool is None:
            raise Exception("Connection pool is not initialized. Call 'initialize()' first.")
        return cls._connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        """Return the connection back to the pool"""
        cls._connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        """Close all the connections in the pool"""
        if cls._connection_pool:
            cls._connection_pool.closeall()
            
    @classmethod
    def execute(cls, query: str, params=None, update=False):
        """Execute a query, optionally commit if it's an update operation"""
        conn = cls.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                if update:
                    conn.commit()
                    return True
                return cursor.fetchall()
        except Exception as error:
            conn.rollback()
            print(f"Error: {error}")
            return None
        finally:
            cls.return_connection(conn)
