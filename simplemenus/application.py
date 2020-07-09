"""Implémentation du controlleur de l'application."""

from .models import Menu, MenuEntry
from .statemachine import SimpleStateMachine
from . import template_environment


class BaseApplication(SimpleStateMachine):
    """Application de base implémentant les détails de bas niveau de 
    l'application, soit la machine à état et les saisies utilisateur.
    """

    def __init__(self, start_state):
        super().__init__(start_state)
        self.choices = {}

    def render(self, menu, template_name, **kwargs):
        """Affiche le menu à l'utilisateur et attend la réponse de ce dernier.

        Le menu est réaffiché tant que l'utilisateur ne choisit pas une
        des options proposées.

        Args:
            menu: objet représentant le menu à afficher
            template_name: nom du fichier de template représentant la vue.
            args: dictionnaire d'arguments contenant les choix de l'utilisateur
        """
        while True:
            # Chargement de la vue via le template
            template = template_environment.get_template(template_name)
            choice = input(template.render(menu=menu, **kwargs))
            if choice in menu:
                self.choices['last'] = self.choices[menu.name] = menu[choice]
                return menu[choice]


class Application(BaseApplication):
    """Représente une application utilisant une système de menus de menus."""

    def __init__(self):
        super().__init__(self.handle_start)

    def handle_start(self):
        menu = (
            Menu("accueil")
            .add("auto", "option 1", self.handle_option1)
            .add("auto", "option 2", self.handle_option2)
            .add("q", "quitter", self.handle_quit)
        )
        return self.render(menu, "menu.txt")

    def handle_option1(self):
        menu = (
            Menu("option1", "accueil > option 1")
            .add("auto", "option 1", self.handle_option1_option1)
            .add("auto", "option 2", self.handle_option1_option2)
            .add("a", "accueil", self.handle_start)
            .add("q", "quitter", self.handle_quit)
        )
        return self.render(menu, "menu.txt")

    def handle_option1_option1(self):
        menu = (
            Menu("option11", "accueil > option 1 > option 1")
            .add("p", "menu précédent", self.handle_option1)
            .add("a", "accueil", self.handle_start)
            .add("q", "quitter", self.handle_quit)
        )
        return self.render(menu, "menu.txt")

    def handle_option1_option2(self):
        menu = (
            Menu("option12", "accueil > option 1 > option 2")
            .add("p", "menu précédent", self.handle_option1)
            .add("a", "accueil", self.handle_start)
            .add("q", "quitter", self.handle_quit)
        )
        return self.render(menu, "menu.txt")

    def handle_option2(self):
        menu = (
            Menu("option2", "accueil > option 2")
            .add("auto", "option 1", self.handle_option2_option1)
            .add("auto", "option 2", self.handle_option2_option2)
            .add("a", "accueil", self.handle_start)
            .add("q", "quitter", self.handle_quit)
        )
        return self.render(menu, "menu.txt")

    def handle_option2_option1(self):
        menu = (
            Menu("option21", "accueil > option 2 > option 1")
            .add("p", "menu précédent", self.handle_option2)
            .add("a", "accueil", self.handle_start)
            .add("q", "quitter", self.handle_quit)
        )
        return self.render(menu, "menu.txt")

    def handle_option2_option2(self):
        menu = (
            Menu("option22", "accueil > option 2 > option 2")
            .add("p", "menu précédent", self.handle_option2)
            .add("a", "accueil", self.handle_start)
            .add("q", "quitter", self.handle_quit)
        )
        return self.render(menu, "menu.txt")

    def handle_quit(self):
        print("Au revoir")
