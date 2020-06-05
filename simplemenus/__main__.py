"""Module de lancement de l'application."""

from .app import Application


def main() -> None:
    """Point d'entrée principal de l'application."""
    application = Application()
    application.start()


if __name__ == "__main__":
    main()
