#!/usr/bin/python
"""Handle jinja2 styled templates"""
import os
import jinja2


def render(file_path, tags):
    """
    Renders a jinja2 styled template file provided by the file_path parameter
    with the values in the tags dictionary parameter. The output is a string.
    """
    abspath = os.path.abspath(file_path)
    if os.path.exists(abspath):
        dirname, filename = os.path.split(abspath)
        loader = jinja2.FileSystemLoader(searchpath=dirname)
        template = jinja2.Environment(loader=loader).get_template(filename)
    else:
        raise ValueError("Template file does not exist: {0}".format(abspath))

    return template.render(tags)
