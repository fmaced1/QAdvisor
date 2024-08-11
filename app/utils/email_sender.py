import smtplib
import os
from email.message import EmailMessage
from email.utils import formataddr
from configparser import ConfigParser

class EmailSender:
    def __init__(self, config_file='../config/config.ini'):
        config = ConfigParser()
        config.read(config_file)

        self.smtp_server = config.get('email', 'smtp_server')
        self.smtp_port = config.get('email', 'smtp_port')
        self.username = config.get('email', 'username')
        self.password = config.get('email', 'password')
        self.sender_email = config.get('email', 'sender_email')
        self.sender_name = config.get('email', 'sender_name')
        self.receiver_email = config.get('email', 'receiver_email')

    def send_text_msg(self, subject: str, msg: str) -> None:
        try:
            message = EmailMessage()
            message['From'] = formataddr((self.sender_name, self.sender_email))
            message['To'] = self.receiver_email
            message['Subject'] = subject
            message.set_content(msg)

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(message)

            print(f"Email successfully sent to {self.receiver_email}")

        except Exception as e:
            print(f"Error sending email message: {e}")
            raise

    def send_photos(self, subject: str, photos: list) -> None:
        try:
            message = EmailMessage()
            message['From'] = formataddr((self.sender_name, self.sender_email))
            message['To'] = self.receiver_email
            message['Subject'] = subject
            message.set_content("Please see the photos attached.")

            for photo_path in photos:
                with open(photo_path, 'rb') as img:
                    img_data = img.read()
                    img_name = os.path.basename(photo_path)
                    message.add_attachment(img_data, maintype='image', subtype='jpeg', filename=img_name)

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.send_message(message)

            print(f"Email with photos successfully sent to {self.receiver_email}")

        except Exception as e:
            print(f"Error sending photos via email: {e}")
            raise