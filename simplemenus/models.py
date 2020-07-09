"""Module implémentant des classes en relations avec le menu."""


class MenuChoice:
    """Représente un choix du menu définie par un objet (item) et un objet
    exécutable permettant de gérer la sélection."""

    def __init__(self, item, handler):
        """Initialise l'entrée du menu avec un choix et une fonction fonction
        qui sera appelée à la sélection de ce choix.

        Args:
            item: objet possédant une méthode __str__ pour l'affichage
            handler: fonction ou méthode à appeler en cas de sélection

        """
        self.item = item
        self.handler = handler

    def __str__(self):
        """Formate le choix représenté par cet objet."""
        return str(self.item)

    def __call__(self):
        """Appelle la fonction de traitement associée au choix."""
        return self.handler()


class Menu:
    """Représente un menu présentant un ou plusieurs choix à l'utilisateur."""

    def __init__(self, name, verbose_name=None):
        """Initialise un nouveau menu vide.

        Args:
            name: nom court du menu courant
            verbose_name (optionnel): nom long du menu. La valeur est fixée à
                celle de name si aucune valeur n'est fournie.

        """
        self.name = name
        self.verbose_name = verbose_name if verbose_name is not None else name
        self._entries = {}
        self._autokey = 1

    def add(self, key, choice, handler):
        """Ajoute une nouvelle option à proposer à l'utilisateur.

        Args:
            key: clé permettant à l'utilisateur de sélectionner l'option.
            choice: objet à proposer comme choix à l'utilisateur.
            handler: fonction ou méthode à appeler en cas de sélection

        Raises:
            Une ValueError est levée si la fonction de traitement  
            fournie pour gérer la sélection du choix ajouté au menu n'est pas
            exécutable.

        """
        if not callable(handler):
            raise ValueError(
                f"The handler provided to handle '{choice}' must be callable"
            )
        if key == "auto":
            key = str(self._autokey)
            self._autokey += 1
        self._entries[key] = MenuChoice(choice, handler)
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
