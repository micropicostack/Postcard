# -*- coding: utf-8 -*-
"""Description"""
import json
import click
from postcard.postcard import Postcard
from postcard.mailer import Mailman
import postcard.templater as templater


@click.command()
@click.argument('entry', nargs=1)
def cli(entry):
    """."""
    try:
        with open(entry) as json_file:
            info = json.loads(json_file.read())
    except FileNotFoundError:
        raise FileNotFoundError("...buuu")

    subject = info['subject']
    sender = info['sender']
    recipients = info['recipients']

    txt_msg = info['plain']
    template = info['template']['path']
    tags = info['template']['tags']

    html_msg = templater.render(template, tags)

    my_postcard = Postcard(subject, sender, recipients)
    my_postcard.create(txt_msg, html_msg)
    my_postcard.add_image(info['images'][0])
    message = my_postcard.package()

    mailman = Mailman(info['host'], info['port'])
    mailman.connect()
    mailman.deliver(sender, recipients, message)

    click.echo('All Done!')
