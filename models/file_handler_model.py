"""Module fom FileHandlerModel Interface"""
import os
from abc import ABC, abstractmethod


class FileHandlerModel(ABC):
    """Class responsible for file operations"""

    def __init__(self, file_path):
        self.__file_name = os.path.basename(file_path)
        self.__file_path = file_path

    @property
    def file_name(self):
        """Method to get JSON file name"""
        return self.__file_name

    @property
    def file_path(self):
        """Method to get JSON file path"""
        return self.__file_path

    @abstractmethod
    def read_data(self, file_path: str = None):
        """Method to read file data."""
        pass

    @abstractmethod
    def write_data(self, data, file_path: str = None):
        """Method to write data to file"""
        pass
