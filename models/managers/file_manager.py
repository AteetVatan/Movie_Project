"""Module for File Manager."""
from enumerations import FileTypes
from models import JsonFileHandlerModel
from models.csv_file_handler_model import CsvFileHandlerModel


class FileManager:
    """FileManager Factory Class."""

    @staticmethod
    def get_file_handler(file_path, file_type = FileTypes.JSON):
        if file_type == FileTypes.JSON:
            return JsonFileHandlerModel(file_path)
        elif file_type == FileTypes.CSV:
            return  CsvFileHandlerModel(file_path)
        else:
            raise ValueError("Unsupported File type")
