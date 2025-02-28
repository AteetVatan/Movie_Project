"""Module to read and write data"""
import json
import os


class FileHandlerModel:
    """Class responsible for file operations"""

    def __init__(self, file_name, filepath):
        self.__file_name = file_name
        self.__file_path = filepath

    @property
    def file_name(self):
        """Method to get JSON file name"""
        return self.__file_name

    @property
    def file_path(self):
        """Method to get JSON file path"""
        return self.__file_path

    def read_data(self, file_path: str = None):
        """Method to read data fo file"""
        d = None
        try:
            if not file_path:
                file_path = self.__file_path

            with open(file_path, encoding="utf-8") as data:
                d = json.load(data)
        except FileNotFoundError as f:
            print(f)
        except IOError as e:
            print("I/O error occurred: ", os.strerror(e.errno))
        return d

    def write_data(self, data, file_path: str = None):
        """Method to write data fo file"""
        try:
            if not file_path:
                file_path = self.__file_path
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError as f:
            print(f)
        except IOError as e:
            print("I/O error occurred: ", os.strerror(e.errno))
        except Exception as e:
            print(e)
