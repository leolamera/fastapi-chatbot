import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_email_dict(receiver_address: str, subject: str):
    message = MIMEMultipart()

    message['From'] = 'lameranha@gmail.com'
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
    session.login('lameranha@gmail.com', 'Lari$$inha1102')
    text = email_dict.as_string()
    session.sendmail('lameranha@gmail.com', receiver_address, text)
    session.quit()
    return []

def send_email(receiver_address: str, subject: str, mail_content: str):
    email_dict = create_email_dict(receiver_address, subject)
    send_text_email(mail_content, email_dict)
    smtp_session(email_dict, receiver_address)
    return []

