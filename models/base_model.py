"""The Base Model Module."""
import os
from abc import ABC, abstractmethod

from enumerations import FileTypes
from helpers import PrintInputHelper as Ph
from models import JsonFileHandlerModel
from models.csv_file_handler_model import CsvFileHandlerModel
from models.managers import FileManager


class BaseModel(ABC):
    """The Base Model Class."""

    def __init__(self, file_path, file_type = FileTypes.JSON):
        self.__file_name = os.path.basename(file_path)
        self.__file_handler = FileManager.get_file_handler(file_path, file_type)
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

    # region CREATE
    @abstractmethod
    def add_data(self, *args):
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
    def delete_data(self):
        """Method to delete the existing movie."""
        return
    # endregion DELETE
