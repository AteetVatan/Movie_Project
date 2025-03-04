"""The Movie App Module."""
from models.storage import IStorage


class MovieApp:
    """The Movie App Class."""

    def __init__(self, storage: IStorage):
        self._storage = storage

    def run(self):
        """Method to run the application."""
        self._storage.menu_controller.start()
