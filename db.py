from pymongo import MongoClient

connection_URI = "mongodb+srv://amirdhesh2003:amirdhesh2453@cluster0.qzsejnk.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_URI)

db = client["librarymanagementsystem"]
