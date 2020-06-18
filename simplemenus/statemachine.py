"""Module implémentant un exemple simpliste de machine à états."""


class SimpleStateMachine:
    """Représente une machine à états simple destinées à implémenter un
    parcours utilisateur dans un système de menus."""

    def __init__(self, start_state):
        """Initialise une nouvelle machine à états."""
        self._next_state: Callable = start_state

    def start(self):
        """Démarre la machine à états."""
        args = {}
        while self._next_state:
            self._next_state, args = self._next_state(**args)
