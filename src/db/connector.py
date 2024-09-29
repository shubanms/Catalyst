import os
import psycopg2

from dotenv import load_dotenv
from psycopg2 import pool

load_dotenv()

class DatabaseConnector:
    _connection_pool = None

    @classmethod
    def initialize(cls):
        """Initialize the connection pool"""
        cls._connection_pool = pool.SimpleConnectionPool(
            minconn=int(os.getenv('DB_MIN_POOL')),
            maxconn=int(os.getenv('DB_MAX_POOL')),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST'),
            port=int(os.getenv('DB_PORT')),
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