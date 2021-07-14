from fastapi import APIRouter, Response

from src.services.orchestrator import webhook_page
from src.models.interfaces import WebEvent

webhook = APIRouter()

@webhook.post('/')
def webhook_frontend(request: WebEvent, response: Response):
    print(request)
    webhook_page(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return []
