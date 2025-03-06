"""The StorageJson Module."""
from models.storage.istorage import IStorage
from controllers import MoviesController, MenuController
from enumerations import FileTypes


# Implement CSV Storage
class StorageCsv(IStorage):
    """The StorageCSV Class."""

    def __init__(self, file_path):
        self.file_path = file_path
        self.data_controller = MoviesController(file_path=file_path, file_type=FileTypes.CSV)
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
