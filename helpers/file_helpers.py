"""Module for File Helpers."""
import os
from enumerations import FileTypes


class FileHelpers:
    """The FileHelpers Class."""
    @staticmethod
    def check_file_type(file_path):
        """Method to """
        file_name = os.path.basename(file_path)
        ext = file_name.rsplit(".", 1)[-1].lower() if "." in file_name else ""
        return FileTypes(ext) if ext in FileTypes._value2member_map_ else FileTypes.UNKNOWN
