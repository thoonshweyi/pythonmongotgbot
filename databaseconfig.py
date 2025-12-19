from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv() 

# Connect to MongoDB
mongo_uri = os.getenv("MONGO_URI","mongodb://localhost:27017/")

#Connect to MongoDB server
client = MongoClient(mongo_uri)
# client = MongoClient(
#      mongo_uri,
#      tls=True,
#      serverSelectionTimeoutMS=20000,
#      connectTimeoutMS=20000
# )
client.admin.command("ping")

# Select database and collection
db = client["mydatabase"]


def dbconnect():
     return db