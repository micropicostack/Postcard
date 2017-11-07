# -*- coding: utf-8 -*-
"""Description"""
import json
import sys
import os
import click
from postcard.postcard import Postcard
from postcard.mailer import Mailman
import postcard.templater as templater


@click.command()
@click.option('--config', type=click.Path(exists=True), help="Path to configuration file")
@click.argument('variant', nargs=1)
def cli(config, variant):
    """."""
    if not config:
        click.echo("Config file not provided, trying to use default")
        cwd = os.path.dirname(os.path.abspath(__file__))
        abspath = os.path.join(cwd, r"..\config.json")
        if os.path.exists(abspath):
            config = abspath
        else:
            click.echo(abspath)
            click.echo("Default config file does not exist!")
            sys.exit(1)

    with open(config) as json_config:
        try:
            info = (json.loads(json_config.read()))[variant]
        except KeyError:
            click.echo("Variant '%s' is not part of the config!" % variant)
            sys.exit(1)

    try:
        subject = info['subject']
        sender = info['sender']
        recipients = info['recipients']

        txt_msg = info['plain']
        template = info['template']['path']
        tags = info['template']['tags']

        host = info['host']
        port = info['port']
        images = info['images']
    except KeyError as err:
        click.echo("Missing required field '%s'" % err.args)
        sys.exit(1)

    html_msg = templater.render(template, tags)

    my_postcard = Postcard(subject, sender, recipients)
    my_postcard.create(txt_msg, html_msg)
    for image in images:
        my_postcard.add_image(image)

    mailman = Mailman(host, port)
    mailman.connect()
    mailman.deliver(sender, recipients, my_postcard.package())

    click.echo('All Done!')
