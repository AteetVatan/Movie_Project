"""Module to create, read and write JSON data"""
import json
import os
from helpers import PrintInputHelper as Ph
from .file_handler_model import FileHandlerModel


class JsonFileHandlerModel(FileHandlerModel):
    """Class responsible for JSON file operations."""

    def __init__(self, file_path):
        if not os.path.exists(file_path):  # Check if a file exists
            self.write_data(data=None, file_path=file_path)

        # self.__metadata = {DataConstants.id(): {
        #     DataConstants.title(): "",
        #     DataConstants.year(): 0,
        #     DataConstants.rating(): 0,
        #     DataConstants.poster(): "",
        #     DataConstants.notes(): "" #optional
        # }}
        super().__init__(file_path)

    def read_data(self, file_path: str = None):
        """Method to read data fo file"""
        d = None
        try:
            if not file_path:
                file_path = self.file_path

            with open(file_path, encoding="utf-8") as data:
                d = json.load(data)
        except FileNotFoundError as f:
            Ph.pr_error(f)
        except IOError as e:
            Ph.pr_error("I/O error occurred: ", os.strerror(e.errno))
        return d

    def write_data(self, data, file_path: str = None):
        """Method to write data to file"""
        try:
            if not file_path:
                file_path = self.file_path
            if data is None:
                data = {}
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError as f:
            Ph.pr_error(f)
        except IOError as e:
            Ph.pr_error("I/O error occurred: ", os.strerror(e.errno))
