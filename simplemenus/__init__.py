"""Initialisation de l'application."""

from jinja2 import Environment, PackageLoader

template_environment = Environment(
    loader=PackageLoader(__name__, 'templates'),
)
