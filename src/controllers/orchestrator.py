from fastapi import APIRouter

from src.services.orchestrator import webhook_page
from src.models.interfaces import WebEvent

webhook = APIRouter()

@webhook.post('/')
def webhook_frontend(request: WebEvent):
    webhook_page(request)
    return []
