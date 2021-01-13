import smtplib, ssl, email.message, email.policy
from keyring import get_password

class Mail:
    def __init__(self):
        self.SMTP_PORT = 587  # For starttls
        self.SMTP_SERVER = "smtp.office365.com"

    def send_email(self,sender, receivers, subject, msg):
        message = email.message.EmailMessage(email.policy.SMTP)
        message['To'] = receivers
        message['From'] = sender
        message['subject'] = subject
        message.set_content(msg)


        context = ssl.create_default_context()
        try:
            with smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT) as server:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(sender, get_password("system", sender))
                server.send_message(message)
        except Exception as e:
            print(e)
