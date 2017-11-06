#!/usr/bin/python
"""."""
import smtplib


class MailmanAuthError(Exception):
    """Authentication error"""


class MailmanSendError(Exception):
    """The SMTP server didn't accept the data."""


class Mailman:
    """This class manages email sending."""
    def __init__(self, host, port, username=None, password=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.server = None

    def connect(self):
        """Connects to the specified host at the specified port.
        Raises:
            ConnectionError if connection fails.
        """
        try:
            self.server = smtplib.SMTP(self.host, self.port)
        except smtplib.socket.gaierror:
            raise ConnectionError("Error connecting to %s" % (self.host))

    def auth(self):
        """Authendicates with the mail server.
        Raises:
            MailmanAuthError when the authentication fails.
        """
        try:
            self.server.login(self.username, self.password)
        except smtplib.SMTPAuthenticationError:
            raise MailmanAuthError("Invalid username (%s) and/or password" % (self.username))

    def deliver(self, sender, recipients, message):
        """Deliver the email message
        Args:
            sender (str): who send the message
            recipients (list): who are the recievers of the message
            message (str): message to be delivered
        Raises:
            MailmanSendError when a SMTPDataError occours
            ConnectionError when sending times out
        """
        if recipients is None:
            raise ValueError('You must specified recipients attribute!')

        try:
            self.server.sendmail(sender, recipients, message)
        except smtplib.SMTPDataError as errormsg:
            raise MailmanSendError("Couldn't send message: %s" % (errormsg))
        except smtplib.socket.timeout:
            raise ConnectionError("Socket error while sending message")
