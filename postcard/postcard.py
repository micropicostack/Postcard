"""Description"""
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from postcard import templater


class Postcard():
    """."""
    def __init__(self, subject, sender, recipients):
        self.subject = subject
        self.sender = sender
        self.recipients = recipients

        self.mail = None
        self.msg_html = None
        self.msg_plain = None

    def new_address(self, subject, sender, recipients):
        """."""
        self.subject = subject
        self.sender = sender
        self.recipients = recipients

        self.mail = None

    def create(self, msg_plain, template, tags):
        """."""
        self.msg_plain = msg_plain
        self.msg_html = templater.render(template, tags)

    def package(self, images=None):
        """."""
        if self.recipients is None:
            raise ValueError('You must specified recipients attribute!')

        self.mail = MIMEMultipart('related')

        self.mail['Subject'] = self.subject
        self.mail['From'] = self.sender
        self.mail['To'] = ','.join(self.recipients)

        self.mail.add_header('Content-Type', 'text/html')

        msg_alt = MIMEMultipart('alternative')
        self.mail.attach(msg_alt)

        msg_alt.attach(MIMEText(self.msg_plain, 'plain'))
        msg_alt.attach(MIMEText(self.msg_html, 'html'))

        if images:
            for key, value in images.items():
                img = MIMEImage(value)
                img.add_header('Content-ID', key)
                self.mail.attach(img)

    def send(self, server, port=0, timeout=10, debug=False):
        """."""
        mailman = smtplib.SMTP(server, port, timeout=timeout)
        try:
            if debug:
                mailman.set_debuglevel(1)

            mailman.sendmail(self.sender, self.recipients, self.mail.as_string())
        # except SMTP error and handle it
        finally:
            mailman.quit()

    def view_card(self):
        """."""
        return self.msg_html

    def view_mail(self):
        """."""
        return self.mail
