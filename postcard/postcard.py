#!/usr/bin/python
"""Description"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from postcard import templater


class Postcard():
    """."""
    def __init__(self, subject, sender, recipients):
        self.subject = subject
        self.sender = sender

        if recipients is None:
            raise ValueError('You must specified recipients attribute!')

        self.recipients = recipients

        self.msg_html = None

    def create(self, template, tags):
        """."""
        self.msg_html = templater.render(template, tags)

    def bundle(self, plain_txt, images=None):
        """."""
        message = MIMEMultipart('related')

        message['Subject'] = self.subject
        message['From'] = self.sender
        message['To'] = ','.join(self.recipients)

        message.add_header('Content-Type', 'text/html')

        msg_alt = MIMEMultipart('alternative')
        message.attach(msg_alt)

        msg_alt.attach(MIMEText(plain_txt, 'plain'))
        msg_alt.attach(MIMEText(self.msg_html, 'html'))

        if images:
            for key, value in images.items():
                img = MIMEImage(value)
                img.add_header('Content-ID', key)
                message.attach(img)

        return message
