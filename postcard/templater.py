#!/usr/bin/python
"""Converter description."""
import os
import jinja2


def render(file_path, tags):
    """
    The function renders a jinja2 styled template file.

    Parameters
    ----------
    file_path: str
        Path to the temaplate file
    tags: dict
        Template tag with the value to be inserted

    Returns
    -------
    str
        Rendered template.

    Raises
    ------
    ValueError
        Provided input file does not exist
    """
    abspath = os.path.abspath(file_path)
    if os.path.exists(abspath):
        dirname, filename = os.path.split(abspath)
        loader = jinja2.FileSystemLoader(searchpath=dirname)
        template = jinja2.Environment(loader=loader).get_template(filename)
    else:
        raise ValueError("Template file does not exist: {0}".format(abspath))

    return template.render(tags)
