from src.config.email_sender import send_email, create_html_template
from src.jobs.watson_manager import get_body_response
from src.models.interfaces import BodyAttendence

async def save_lead(input_text: str, feedback_response):
    receiver_address = 'lameranha@gmail.com'
    subject = '📪 Um novo Lead acabou de se cadastrar'

    body = get_body_response(feedback_response)
    name = body['name']
    email = body['email']
    whatsapp = body['whatsapp']


    html_template = create_html_template('lead', name, email, whatsapp)
    

    if '@' in input_text:
        mail_content = f'email: {input_text}'
        await send_email(receiver_address, subject, mail_content)
        return 'Consegui liberar seu cupom'

    mail_content = f'telefone: {input_text}'
    await send_email(receiver_address, subject, html_template)
    return 'Consegui liberar seu cupom'

async def store_attendance(input_text, feedback_response):
    receivers_address = ['lameranha@gmail.com', 'contatoencaracolados@gmail.com']
    subject = '🤫 Uma nova solicitação de atendimento chegou'

    body: BodyAttendence = get_body_response(feedback_response)

    name = body['name']
    type = body['type']
    email = body['email']
    whatsapp = body['phone']
    obs = body['obs']


    html_template = create_html_template('attend', name, email, whatsapp, type, obs)

    mail_content = f'nome completo: {name}\n email: {email}\n assunto: {type}\n'
    for receiver_address in receivers_address:
        await send_email(receiver_address, subject, html_template)
        return 'Criando ticket de atendimento ...'


