from src.db.loader.user import UserDataLoader
from src.schemas.user import NewUser, UserCredentials
from src.schemas.schemas import Error
from src.utils.util import user_exists
from src.services.auth import generate_jwt
from src.utils.util import hash_password

database = UserDataLoader()

def register_new_user(new_user: NewUser):
    if database.username_exists(new_user.username):
        return Error(message="Username already exists!")
    
    user = UserCredentials(username=new_user.username, password=new_user.password)
    
    new_user.password = hash_password(new_user.password)
    database.register_user(new_user)
    
    if user_exists(user):
        return generate_jwt(user)
