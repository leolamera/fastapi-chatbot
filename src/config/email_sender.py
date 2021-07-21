import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os

outlook_password = os.environ.get('outlook_password')


print(outlook_password)

def create_email_dict(receiver_address: str, subject: str):
    message = MIMEMultipart()

    message['From'] = 'neural-chat@outlook.com'
    message['To'] = receiver_address
    message['Subject'] = subject
    
    return message

def send_text_email(mail_content: str, email_dict: MIMEMultipart): 
    email_dict.attach(MIMEText(mail_content, 'plain'))
    return []

async def smtp_session(email_dict: MIMEMultipart, receiver_address: str):
    session = smtplib.SMTP('smtp.office365.com',587)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login('neural-chat@outlook.com', outlook_password)
    text = email_dict.as_string()
    session.sendmail('neural-chat@outlook.com', receiver_address, text)
    session.quit()
    session.close()
    return []

async def send_email(receiver_address: str, subject: str, mail_content: str):
    email_dict = create_email_dict(receiver_address, subject)
    send_text_email(mail_content, email_dict)
    await smtp_session(email_dict, receiver_address)
    return []

