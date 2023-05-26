import os
from fastapi_mail import  ConnectionConfig
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from utils.send_template_email import template_mail

# Load environment variables
load_dotenv()
#admin@luminis.mx
#Lumi@2023

# Load variables from .env file
class Envs:
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_FROM = os.getenv('MAIL_FROM')
    MAIL_PORT = int(os.getenv('MAIL_PORT'))
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_FROM_NAME = os.getenv('MAIN_FROM_NAME')


""" conf = ConnectionConfig(
    MAIL_USERNAME=Envs.MAIL_USERNAME,
    MAIL_PASSWORD=Envs.MAIL_PASSWORD,
    MAIL_FROM=Envs.MAIL_FROM,
    MAIL_PORT=int(Envs.MAIL_PORT),
    MAIL_SERVER=Envs.MAIL_SERVER,
    MAIL_FROM_NAME=Envs.MAIL_FROM_NAME,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    TEMPLATE_FOLDER=os.path.join(os.getcwd(), 'templates/email')
            ) """

def send_email(to, subject, body):
    try:
        # create message object instance
        msg = MIMEMultipart()
        message = body

        # setup the parameters of the message
        msg['From'] = Envs.MAIL_FROM
        msg['To'] = to
        msg['Subject'] = subject

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # Configura los parámetros de conexión SMTP
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = Envs.MAIL_USERNAME
        smtp_password = Envs.MAIL_PASSWORD

        # establece la conexión con el servidor
        server = smtplib.SMTP(host=smtp_server, port=smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # envía el mensaje
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print("successfully sent email to %s:" % (msg['To']))
        return True
    except Exception as e:
        print("Error: unable to send email")
        print(e)
        return False
    