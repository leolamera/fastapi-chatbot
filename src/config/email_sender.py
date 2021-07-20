import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os

gmail_password = os.environ.get('gmail_password')
print(gmail_password)

def create_email_dict(receiver_address: str, subject: str):
    message = MIMEMultipart()

    message['From'] = 'datajus.services@gmail.com'
    message['To'] = receiver_address
    message['Subject'] = subject
    
    return message

def send_text_email(mail_content: str, email_dict: MIMEMultipart): 
    email_dict.attach(MIMEText(mail_content, 'plain'))
    return []

def smtp_session(email_dict: MIMEMultipart, receiver_address: str):
    session = smtplib.SMTP("smtp.gmail.com", 587)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login('datajus.services@gmail.com', gmail_password)
    text = email_dict.as_string()
    session.sendmail('datajus.services@gmail.com', receiver_address, text)
    session.quit()
    session.close()
    return []

def send_email(receiver_address: str, subject: str, mail_content: str):
    email_dict = create_email_dict(receiver_address, subject)
    send_text_email(mail_content, email_dict)
    smtp_session(email_dict, receiver_address)
    return []

