"""Initialisation de l'application."""

from jinja2 import Environment, PackageLoader

# initialisation de l'environnement pour le moteur de templates (jinja)
template_environment = Environment(
    loader=PackageLoader(__name__, 'templates'),
)
