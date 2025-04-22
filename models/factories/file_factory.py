"""Module for File Manager."""
from enumerations import FileTypes
from models.handlers import JsonFileHandlerModel
from models.handlers import CsvFileHandlerModel


class FileFactory:
    """File Factory Class."""
    @staticmethod
    def get_file_handler(file_path, file_type=FileTypes.JSON):
        """Factory Method to create the respective File Handler instance base on FileTypes."""
        if file_type == FileTypes.JSON:
            return JsonFileHandlerModel(file_path)
        if file_type == FileTypes.CSV:
            return CsvFileHandlerModel(file_path)
        raise ValueError("Unsupported File type")
