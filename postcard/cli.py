# -*- coding: utf-8 -*-
"""Description"""
import os
import json
import click
from postcard.postcard import Postcard


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

    card.create(plain_text, template, tags)

    images = {}
    with open(info['images'][0]['path'], 'rb') as img_file:
        images[info['images'][0]['key']] = img_file.read()

    card.package(images)

    card.send(info['host'], info['port'], timeout=10)
    click.echo('All Done!')
