import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(sender, password, receiver, subject, body, is_html=False, attachment_path=None):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'html' if is_html else 'plain'))

        # Attachment
        if attachment_path and os.path.exists(attachment_path):
            with open(attachment_path, "rb") as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())

            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(attachment_path)}')
            msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)

        server.send_message(msg)
        server.quit()

        return True, "Sent"

    except Exception as e:
        return False, str(e)