#!/usr/bin/python
"""."""
import smtplib


class MailmanAuthError(Exception):
    """."""


class MailmanSendError(Exception):
    """."""


class Mailman:
    """."""
    def __init__(self, host, port, username=None, password=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.server = None

    def connect(self):
        """Connects to the specified host at the specified port.
        Raises ConnectionError if not possible."""
        try:
            self.server = smtplib.SMTP(self.host, self.port)
        except smtplib.socket.gaierror:
            raise ConnectionError("Error connecting to %s" % (self.host))

    def auth(self):
        """Authendicates with the mail server. Raises MailmanAuthError
        when the authentication fails."""
        try:
            self.server.login(self.username, self.password)
        except smtplib.SMTPAuthenticationError:
            raise MailmanAuthError("Invalid username (%s) and/or password" % (self.username))

    def deliver(self, sender, recipients, message):
        """."""
        if recipients is None:
            raise ValueError('You must specified recipients attribute!')

        try:
            self.server.sendmail(sender, recipients, message.as_string())
        except smtplib.SMTPDataError as errormsg:
            raise MailmanSendError("Couldn't send message: %s" % (errormsg))
        except smtplib.socket.timeout:
            raise ConnectionError("Socket error while sending message")
