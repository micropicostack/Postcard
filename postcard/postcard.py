#!/usr/bin/python
"""Description"""
import os
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
        """Create the multipart email message
        Args:
            txt_msg (str): message in plain text format
            html_msg (str): message in html format
        """
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
        """Adds an image to the message in the cid format.
        Args:
            image (tuple): the image should be in the (key, path) format
        Raises:
            ValueError when the file does not exist
        """
        key, filepath = image
        abspath = os.path.abspath(filepath)

        if os.path.exists(abspath):
            with open(abspath, 'rb') as image_file:
                img = image_file.read()
            cid = MIMEImage(img)
            cid.add_header('Content-ID', key)
            self.message.attach(cid)
        else:
            raise ValueError("The path %s does not exist!" % abspath)

    def add_file(self):
        """."""
        pass

    def package(self):
        """Return the email message as a string"""
        return self.message.as_string()
