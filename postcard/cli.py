# -*- coding: utf-8 -*-
"""Description"""
import json
import click
from postcard.postcard import Postcard
from postcard.mailer import Mailman


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

    card = Postcard(subject, sender, recipients)

    plain_text = info['plain']
    template = info['template']['path']
    tags = info['template']['tags']

    try:
        card.create(template, tags)
    except ValueError as error:
        click.echo(error)
        return 0

    images = {}
    with open(info['images'][0]['path'], 'rb') as img_file:
        images[info['images'][0]['key']] = img_file.read()

    message = card.bundle(plain_text, images)

    mailman = Mailman(info['host'], info['port'])
    mailman.connect()
    mailman.deliver(sender, recipients, message)

    click.echo('All Done!')

# my_postcard = Postcard(subject, sender, recipients)
# my_postcard.create(postcard_template, template_vars)
# message = postcard.attach(plain, images)
# mailman = Mailman(host, port)
# mailman.connect()
# mailman.deliver(subject, sender, recipients, message)