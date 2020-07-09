from . import template_environment


class BaseApplication:
    """Application de base implémentant les détails de bas niveau de 
    l'application, soit la machine à état et les saisies utilisateur.
    """

    def __init__(self, start_menu):
        self.next_menu = start_menu
        self.choices = {}

    def render(self, menu, template_name, **kwargs):
        """Affiche le menu à l'utilisateur et attend la réponse de ce dernier.

        Le menu est réaffiché tant que l'utilisateur ne choisit pas une
        des options proposées.

        Args:
            menu: objet représentant le menu à afficher
            template_name: nom du fichier de template représentant la vue
            kargs: dictionnaire d'arguments à envoyer au template

        """
        while True:
            # Chargement de la vue via le template
            template = template_environment.get_template(template_name)
            choice = input(template.render(menu=menu, **kwargs))
            if choice in menu:
                self.choices['last'] = self.choices[menu.name] = menu[choice]
                return menu[choice].handler

    def start(self):
        """Démarre l'application."""
        while self.next_menu:
            self.next_menu = self.next_menu()
