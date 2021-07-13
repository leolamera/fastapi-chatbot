from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class WebEvent(BaseModel):
    _id: Optional[ObjectId]
    eventId: str
    message: str
    username: str
    serverOrigin: bool

class Context(BaseModel):
    _id: Optional[ObjectId]
    eventId: str
    watsonSession: Optional[str]

class Status(BaseModel):
    _id: Optional[ObjectId]
    eventId: str
    status: str

class WatsonResponse(BaseModel):
    session_id: str
    event_id: str
    message: str