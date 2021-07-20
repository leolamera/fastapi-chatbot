from fastapi import APIRouter, Response

from src.services.orchestrator import webhook_page
from src.models.interfaces import WebEvent
from src.config.email_sender import send_email

webhook = APIRouter()

@webhook.post('/')
def webhook_frontend(request: WebEvent, response: Response):
    webhook_page(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return []

@webhook.get('/email')
def send_email_function():
    send_email('datajus.services@gmail.com', 'tete e-mail', 'olá pessoa, tudo de bom')
    return {'mensagem': 'email enviado'}


