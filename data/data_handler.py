"""Module to read and write data"""
import json
import os


class DataHandler:
    """Class responsible for data operations"""
    __json_file_name = "movie.json"
    __json_file_path = os.path.join(os.getcwd(), "data", __json_file_name)

    @classmethod
    def json_file_name(cls):
        """Method to get Json file name"""
        return cls.__json_file_name

    @staticmethod
    def read_data(file_path: str = __json_file_path):
        """Method to read data fo file"""
        d = None
        try:
            with open(file_path, encoding="utf-8") as data:
                d = json.load(data)
        except FileNotFoundError as f:
            print(f)
        except IOError as e:
            print("I/O error occurred: ", os.strerror(e.errno))
        return d

    @staticmethod
    def write_data(data: dict, file_path: str = __json_file_path):
        """Method to write data fo file"""
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError as f:
            print(f)
        except IOError as e:
            print("I/O error occurred: ", os.strerror(e.errno))
