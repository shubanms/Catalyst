from src.db.database_loader import DataBaseLoader

database = DataBaseLoader()

data = database.get_user_topics("shubanms")
print(data)

