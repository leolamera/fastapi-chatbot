from pymongo import MongoClient

client = MongoClient()
db = client["dev"]

contexts_collection = db["context"]
status_collection = db["status"]
events_collection = db["events"]