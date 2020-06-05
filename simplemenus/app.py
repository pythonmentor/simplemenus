"""Implémentation de l'application elle-même."""

from typing import Any, Dict, Tuple

from .menus import Menu, MenuEntry
from .statemachine import SimpleStateMachine


class Application(SimpleStateMachine):
    """Représente une application utilisant une système de menus de menus."""

    def __init__(self) -> None:
        super().__init__(self.handle_start)

    def handle_start(self, **args: Any) -> Tuple[MenuEntry, Dict]:
        return (
            Menu("accueil")
            .add("auto", "option 1", self.handle_option1)
            .add("auto", "option 2", self.handle_option2)
            .add("q", "quitter", self.handle_quit)
            .render(args)
        )

    def handle_option1(self, **args: Any) -> Tuple[MenuEntry, Dict]:
        return (
            Menu("option1", "accueil > option 1")
            .add("auto", "option 1", self.handle_option1_option1)
            .add("auto", "option 2", self.handle_option1_option2)
            .add("a", "accueil", self.handle_start)
            .add("q", "quitter", self.handle_quit)
            .render(args)
        )

    def handle_option1_option1(self, **args: Any) -> Tuple[MenuEntry, Dict]:
        return (
            Menu("option11", "accueil > option 1 > option 1")
            .add("p", "menu précédent", self.handle_option1)
            .add("a", "accueil", self.handle_start)
            .add("q", "quitter", self.handle_quit)
            .render(args)
        )

    def handle_option1_option2(self, **args: Any) -> Tuple[MenuEntry, Dict]:
        return (
            Menu("option12", "accueil > option 1 > option 2")
            .add("p", "menu précédent", self.handle_option1)
            .add("a", "accueil", self.handle_start)
            .add("q", "quitter", self.handle_quit)
            .render(args)
        )

    def handle_option2(self, **args: Any) -> Tuple[MenuEntry, Dict]:
        return (
            Menu("option2", "accueil > option 2")
            .add("auto", "option 1", self.handle_option2_option1)
            .add("auto", "option 2", self.handle_option2_option2)
            .add("a", "accueil", self.handle_start)
            .add("q", "quitter", self.handle_quit)
            .render(args)
        )

    def handle_option2_option1(self, **args: Any) -> Tuple[MenuEntry, Dict]:
        return (
            Menu("option21", "accueil > option 2 > option 1")
            .add("p", "menu précédent", self.handle_option2)
            .add("a", "accueil", self.handle_start)
            .add("q", "quitter", self.handle_quit)
            .render(args)
        )

    def handle_option2_option2(self, **args: Any) -> Tuple[MenuEntry, Dict]:
        return (
            Menu("option22", "accueil > option 2 > option 2")
            .add("p", "menu précédent", self.handle_option2)
            .add("a", "accueil", self.handle_start)
            .add("q", "quitter", self.handle_quit)
            .render(args)
        )

    def handle_quit(self, **args: Any):
        print("Au revoir")
        return None, args
