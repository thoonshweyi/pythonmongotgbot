from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv() 

# Connect to MongoDB
mongo_uri = os.getenv("MONGO_URI","mongodb://localhost:27017/")

#Connect to MongoDB server
client = MongoClient(mongo_uri)

# Select database and collection
db = client["mydatabase"]


def dbconnect():
     return db