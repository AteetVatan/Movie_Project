"""The StorageJson Module."""
from models.storage.istorage import IStorage
from controllers import MenuController
from controllers.movies_cli_controller import MoviesCliController
from enumerations import FileTypes


class StorageJson(IStorage):
    """The StorageJson Class."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.data_controller = MoviesCliController(file_path=file_path, file_type=FileTypes.JSON)
        self.menu_controller = MenuController(self.data_controller)

    def list_movies(self):
        """Method to list data."""
        self.data_controller.list_data()

    def add_movie(self):
        """Method to add data."""
        self.data_controller.add_data()

    def delete_movie(self):
        """Method to delete data."""
        self.data_controller.delete_data()

    def update_movie(self):
        """Method to update data Notes."""
        self.data_controller.update_data()
