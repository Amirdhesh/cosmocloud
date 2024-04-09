from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("connection_URI"))

db = client["librarymanagementsystem"]
