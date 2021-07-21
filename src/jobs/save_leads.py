from src.config.email_sender import send_email
from src.jobs.watson_manager import get_body_response
from src.models.interfaces import BodyAttendence

async def save_lead(input_text: str, feedback_response=None):
    receiver_address = 'lameranha@gmail.com'
    subject = '📪 Um novo Lead acabou de se cadastrar'
    

    if '@' in input_text:
        mail_content = f'email: {input_text}'
        await send_email(receiver_address, subject, mail_content)
        return 'Consegui liberar seu cupom'

    mail_content = f'telefone: {input_text}'
    await send_email(receiver_address, subject, mail_content)
    return 'Consegui liberar seu cupom'

async def store_attendance(input_text, feedback_response):
    receivers_address = ['lameranha@gmail.com', 'contatoencaracolados@gmail.com']
    subject = '🤫 Uma nova solicitação de atendimento chegou'

    body: BodyAttendence = get_body_response(feedback_response)
    name = body['name']
    type = body['type']
    email = body['email']

    mail_content = f'nome completo: {name}\n email: {email}\n assunto: {type}\n'
    for receiver_address in receivers_address:
        await send_email(receiver_address, subject, mail_content)
        return 'Criando ticket de atendimento ...'


