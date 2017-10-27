#!/usr/bin/python
"""Converter description."""
import os
import jinja2


class Converter():
    """Converter class."""
    def __init__(self):
        self.template = None

    def setup(self, template_file):
        """
        Args:
            template_file: Path to the jinja style template file.
        Raises:
            ValueError: Provided input file does not exist
        """
        abspath = os.path.abspath(template_file)
        if os.path.exists(abspath):
            dirname, filename = os.path.split(abspath)
            loader = jinja2.FileSystemLoader(searchpath=dirname)
            self.template = jinja2.Environment(loader=loader).get_template(filename)
        else:
            raise ValueError("Template file does not exist: {file}".format(file=abspath))

    def render(self, template_data):
        """
        The render method provides the input data to the jinja2 renderer.

        Args:
            template_data: Type dictionary, used to populate the template.
        Returns:
            Rendered output as a string.
        """
        return self.template.render(template_data)
