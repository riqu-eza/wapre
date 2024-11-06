from pymongo import MongoClient
from ..config.Config import DATABASE_URI

client = MongoClient(DATABASE_URI)
db = client.wapre

def init_db():
    # Here you can initialize collections or perform setup tasks
    print("Database initialized.")
