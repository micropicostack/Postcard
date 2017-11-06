#!/usr/bin/python
"""Description"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


class Postcard():
    """."""
    def __init__(self, subject, sender, recipients):
        self.subject = subject
        self.sender = sender

        if not recipients:
            raise ValueError('You must specified recipients attribute!')

        self.recipients = recipients
        self.message = None

    def create(self, txt_msg, hmtl_msg):
        """."""
        self.message = MIMEMultipart('related')

        self.message['Subject'] = self.subject
        self.message['From'] = self.sender
        self.message['To'] = ','.join(self.recipients)

        self.message.add_header('Content-Type', 'text/html')

        msg_alt = MIMEMultipart('alternative')
        self.message.attach(msg_alt)

        msg_alt.attach(MIMEText(txt_msg, 'plain'))
        msg_alt.attach(MIMEText(hmtl_msg, 'html'))

    def add_image(self, image):
        """."""
        key, file_path = image
        with open(file_path, 'rb') as f:
            img = f.read()
        cid = MIMEImage(img)
        cid.add_header('Content-ID', key)
        self.message.attach(cid)

    def add_file(self):
        """."""
        pass

    def package(self):
        """."""
        return self.message.as_string()
