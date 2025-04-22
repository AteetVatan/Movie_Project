"""The Base Model Module."""
from abc import ABC, abstractmethod

from config import config
from helpers.api_helper import ApiHelper
from models.api_request_model import ApiRequestModel
from models.managers import DataManagerInterface


class BaseModel(ABC):
    """The Base Model Class."""
    __api_handler: ApiHelper = None
    __api_request_model: ApiRequestModel = None
    __data_manager: DataManagerInterface = None

    def __init__(self, data_manager: DataManagerInterface):
        self.__data_manager = data_manager
        if config.USE_MOVIE_API:
            if not self.__api_request_model:
                self.__api_request_model = ApiRequestModel()
            self.__api_handler = ApiHelper(self.__api_request_model)
        self.__data = self.__data_manager.read_data()

    @property
    def data(self):
        """The main data property getter"""
        return self.__data

    @data.setter
    def data(self, data):
        """The main data property setter"""
        self.__data = data

    @property
    def api_handler(self):
        """The file_handler object getter"""
        return self.__api_handler

    # region CREATE
    @abstractmethod
    def get_imdb_data(self, **kwargs):
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
