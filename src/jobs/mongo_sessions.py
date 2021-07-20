from src.config.database_mongo import events_collection, contexts_collection, status_collection
from src.models.interfaces import WebEvent, Context, Status

# EVENTS
def store_event(data: WebEvent):
    dict_data = dict(data)
    return events_collection.insert_one(dict_data)

def find_event_by_id(event_id: str):
    return events_collection.find_one({ 'eventId': event_id })

# CONTEXT
def store_context(data: Context):
    dict_data = dict(data)
    return contexts_collection.insert_one(dict_data)

def find_store_context_by_id(event_id: str):
    return contexts_collection.find_one({ 'eventId': event_id })

# STATUS
def store_status(data: Status):
    dict_data = dict(data)
    return status_collection.insert_one(dict_data)

def find_status_by_id(event_id: str):
    return status_collection.find_one({ 'eventId': event_id })

