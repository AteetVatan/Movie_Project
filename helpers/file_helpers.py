"""Module for File Helpers."""
import os
import mimetypes
from config import config
from enumerations import FileTypes


class FileHelpers:
    """The FileHelpers Class."""

    @staticmethod
    def get_file_type_from_file_types_enum(file_path):
        """Method to return a file type from FileTypes Enum"""
        file_name = os.path.basename(file_path)
        ext = file_name.rsplit(".", 1)[-1].lower() if "." in file_name else ""
        return FileTypes(ext) if ext in FileTypes._value2member_map_ else FileTypes.UNKNOWN

    @staticmethod
    def get_file_extension(file_name):
        """Method to file extension."""
        ext = file_name.rsplit(".", 1)[-1].lower() if "." in file_name else ""
        return ext

    @staticmethod
    def get_data_file_path(file_name):
        """Method to get the data file path"""
        return os.path.join(os.getcwd(), config.DATA_DIRECTORY, file_name)

    @staticmethod
    def get_file_type_from_file_data(file_path):
        """Method to check filetype from file data"""
        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type:
            if mime_type in ["application/json", "text/json"]:
                return FileTypes.JSON

            if mime_type in ["application/csv", "text/csv"]:
                return FileTypes.CSV

        return FileTypes.UNKNOWN

    @staticmethod
    def file_correction(file_name):
        """Method to correct the file name"""
        ext = FileHelpers.get_file_extension(file_name)
        file_path = FileHelpers.get_data_file_path(file_name)

        if os.path.exists(file_path):
            file_type: FileTypes = FileHelpers.get_file_type_from_file_data(file_path)
            if file_type == ext:
                # the file passed validation and is correct
                return file_name

        if ext in [FileTypes.JSON.value, FileTypes.CSV.value]:
            return file_name

        # the file type does not meet the extension
        return os.path.splitext(file_name)[0] + ".json"  # default file type
