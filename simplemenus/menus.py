"""Module implémentant des classes en relations avec le menu."""

from typing import Any, Callable, Dict, List, Optional, Tuple


class MenuEntry:
    """Représente une entrée de menu contenant définie par un objet (item) et
    l'état suivant, si l'entrée est sélectionnée.

    Attributs:
        item: objet possédant une méthode __str__ pour l'affichage
        next: fonction ou méthode implémentant le menu suivant
    """

    def __init__(self, item: Any, next_state: Callable) -> None:
        """Initialise l'entrée du menu avec un item, une méthode jouant le rôle
        d'état suivant et un lien vers le menu.

        Args:
            item: objet possédant une méthode __str__ pour l'affichage
            next_state: fonction ou méthode implémentant le menu suivant
        """
        self.item: Any = item
        self.next: Callable = next_state

    def __str__(self) -> str:
        """Formate l'entrée pour son affichage au sein du menu."""
        return str(self.item)

    def __call__(self, **args) -> Tuple["MenuEntry", Dict]:
        """Executes the next state."""
        return self.next(**args)


class Menu:
    """Représente un menu présentant un ou plusieurs options à
    l'utilisateur."""

    def __init__(self, name: str, verbose_name: Optional[str] = None) -> None:
        """Initialise un nouveau menu vide.

        Args:
            name: nom court du menu courant
            verbose_name: titre à affiche en haut du menu.
        """
        self._name = name
        self._verbose_name = verbose_name if verbose_name is not None else name
        self._entries: Dict = {}
        self._autokey: int = 1

    def add(self, key: str, item: Any, next: Callable) -> "Menu":
        """Ajoute une nouvelle option à proposer à l'utilisateur.

        Args:
            key: clé permettant à l'utilisateur de sélectionner l'option.
            item: objet à proposer à l'utilisateur.
            next: état à exécuter si l'option est
                sélectionnée par l'utilisateur.
        """
        if key == "auto":
            key = str(self._autokey)
            self._autokey += 1
        key = key.lower().strip()
        self._entries[key] = MenuEntry(item, next)
        return self

    def add_many(self, items: List, next: Callable) -> "Menu":
        """Ajouter plusieurs options auto-numérotées.

        Args:
            items: liste d'options à ajouter
            next: état à exécuter si une de ces options est
                sélectionnée.
        """
        for item in items:
            self.add("auto", item, next)

        return self

    def __str__(self) -> str:
        """Formate le menu en vue de sa présentation à l'utilisateur."""
        lines: List[str] = [f"{self._verbose_name.title()}\n"]
        for key, value in self._entries.items():
            lines.append(f"{key} - {value}")
        lines.append("")
        lines.append(">>> ")
        return "\n".join(lines)

    def render(self, args: Dict) -> Tuple[MenuEntry, Dict]:
        """Affiche le menu à l'utilisateur et attend la réponse de ce dernier.

        Le menu est réaffiché tant que l'utilisateur ne choisit pas une
        des options proposées.
        """
        entries: Dict = self._entries
        while True:
            choice = input(self).lower().strip()
            if choice in entries:
                args['last'] = args[self._name] = entries[choice]
                return entries[choice], args
