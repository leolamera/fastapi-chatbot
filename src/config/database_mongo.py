from pymongo import MongoClient
import os

print(os.environ.get('mongo_uri'))

mongo_uri = 'mongodb+srv://apicrud:a9BB3bxoI69iR4YB@neural-chat-db.gcvan.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

client = MongoClient(mongo_uri)
db = client["dev"]

contexts_collection = db["context"]
status_collection = db["status"]
events_collection = db["events"]