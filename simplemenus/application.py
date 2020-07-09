"""Implémentation du controlleur de l'application."""

from .controllers import BaseApplication
from .models import Menu


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
