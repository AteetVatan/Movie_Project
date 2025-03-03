from controllers import MoviesController, MenuController
from enumerations import FileTypes
from models.storage import IStorage


# Implement CSV Storage
class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        self.__data_controller = MoviesController(file_path=file_path, file_type=FileTypes.CSV)
        self.__menu_controller = MenuController(self.__data_controller)

    @property
    def menu_controller(self):
        return self.__menu_controller

    def list_movies(self):
        self.__data_controller.list_data()

    def add_movie(self):
        self.__data_controller.add_data()

    def delete_movie(self, title):
        self.__data_controller.delete_data(title=title)

    def update_movie(self, title, rating):
        self.__data_controller.update_data(title=title, rating=rating)