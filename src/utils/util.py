import hashlib

from src.schemas.schemas import User
from src.db.database_loader import DataBaseLoader

database = DataBaseLoader()

def hash_password(password: str):
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    return password_hash


def user_exists(user_data: User):
    user_details = database.get_user_details(user_data.username)
    
    hashed_password = hash_password(user_data.password)
    
    if user_details and user_details.password_hash == hashed_password:
        return True
    else:
        return False
