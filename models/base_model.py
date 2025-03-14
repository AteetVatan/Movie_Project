"""The Base Model Module."""
from abc import ABC, abstractmethod

from config import config
from enumerations import FileTypes
from helpers.api_helper import ApiHelper
from models.api_request_model import ApiRequestModel
from models.managers import FileManager


class BaseModel(ABC):
    """The Base Model Class."""
    __api_handler: ApiHelper = None
    __api_request_model: ApiRequestModel = None

    def __init__(self, file_path, file_type = FileTypes.JSON):
        self.__file_handler = FileManager.get_file_handler(file_path, file_type)
        if config.USE_DATA_FROM_API:
            if not self.__api_request_model:
                self.__api_request_model = ApiRequestModel()
            self.__api_handler = ApiHelper(self.__api_request_model)
        self.__data = self.file_handler.read_data()

    @property
    def data(self):
        """The main data property getter"""
        return self.__data

    @data.setter
    def data(self, data):
        """The main data property setter"""
        self.__data = data

    @property
    def file_handler(self):
        """The file_handler object getter"""
        return self.__file_handler

    @property
    def api_handler(self):
        """The file_handler object getter"""
        return self.__api_handler

    # region CREATE
    @abstractmethod
    def add_data(self, **kwargs):
        """Adds data."""
        return

    # endregion CREATE

    # region READ
    @abstractmethod
    def list_data(self):
        """Prints the data in a list."""
        return

    # endregion READ

    # region UPDATE

    @abstractmethod
    def update_data(self):
        """Method to Update data."""
        return

    def save_data(self):
        """Method to save data."""
        return

    # endregion UPDATE

    # region DELETE
    @abstractmethod
    def delete_data(self, title):
        """Method to delete the existing movie."""
        return
    # endregion DELETE
