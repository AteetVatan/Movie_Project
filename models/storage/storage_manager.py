"""Module for storage Factory"""
import sys

from enumerations import FileTypes
from models.storage import StorageJson, StorageCsv, IStorage
from helpers import PrintInputHelper as Ph, FileHelpers


class StorageManager:
    """Factory class to create storage Type."""

    def __init__(self, file_path):
        self.__storage = None
        file_type = FileHelpers.check_file_type(file_path)
        self.__storage_factory(file_path, file_type)

    @property
    def storage(self) -> IStorage:
        """Property to get the data storage instance."""
        return self.__storage

    def __storage_factory(self, file_path, file_type=FileTypes.JSON):
        """Method to create Storage."""
        try:
            if file_type == FileTypes.JSON:
                self.__storage = StorageJson(file_path)
            elif file_type == FileTypes.CSV:
                self.__storage = StorageCsv(file_path)
            else:
                raise ValueError("Unsupported storage type")
        except (ValueError, KeyError, TypeError) as e:
            Ph.pr_error(e.args[0])
            sys.exit(1)  # Exit program with failure code
