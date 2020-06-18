"""Module implémentant des classes en relations avec le menu."""


class MenuEntry:
    """Représente une entrée de menu définie par un objet (item) et un callable
    représentant l'état suivant."""

    def __init__(self, item, next_state):
        """Initialise l'entrée du menu avec un item et une méthode jouant le
        rôle d'état suivant.

        Args:
            item: objet possédant une méthode __str__ pour l'affichage
            next_state: fonction ou méthode implémentant le menu suivant
        """
        self.item = item
        self.next = next_state

    def __str__(self):
        """Formate l'entrée pour son affichage au sein du menu."""
        return str(self.item)

    def __call__(self, **args):
        """Executes the next state."""
        return self.next(**args)


class Menu:
    """Représente un menu présentant un ou plusieurs options à
    l'utilisateur."""

    def __init__(self, name, verbose_name=None):
        """Initialise un nouveau menu vide.

        Args:
            name: nom court du menu courant
            verbose_name: titre à affiche en haut du menu.
        """
        self.name = name
        self.verbose_name = verbose_name if verbose_name is not None else name
        self._entries = {}
        self._autokey = 1

    def add(self, key, item, next):
        """Ajoute une nouvelle option à proposer à l'utilisateur.

        Args:
            key: clé permettant à l'utilisateur de sélectionner l'option.
            item: objet à proposer à l'utilisateur.
            next: état à exécuter si l'option est sélectionnée.
        """
        if key == "auto":
            key = str(self._autokey)
            self._autokey += 1
        self._entries[key] = MenuEntry(item, next)
        return self

    def __contains__(self, key):
        """Supporte l'opérateur in sur le menu."""
        return key in self._entries

    def __iter__(self):
        """Permet d'itérer sur les couples (clé, entrée) du menu."""
        return iter(self._entries.items())

    def __getitem__(self, key):
        """Accède à l'entrée de menu correspondante à la clé."""
        return self._entries[key]
