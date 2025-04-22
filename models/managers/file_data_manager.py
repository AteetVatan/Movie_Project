"""File-based implementation of the DataManagerInterface for movie management."""

from enumerations import FileTypes
from models.factories import FileFactory
from models.utils import DataUtils
from .data_manager_interface import DataManagerInterface


class FileDataManager(DataManagerInterface):
    """Wraps MovieModel (JSON/CSV) with a unified interface."""

    def __init__(self, file_path="", file_type=FileTypes.JSON):
        """Initialize file handler based on file type (JSON/CSV)."""
        self.__file_handler = FileFactory.get_file_handler(file_path, file_type)

    # region READ
    def read_data(self):
        """Read and return data from the file."""
        return self.__file_handler.read_data()

    def get_all_users(self):
        """Get all users (not supported in file mode)."""
        raise NotImplementedError("User management is not supported in FileDataManager.")

    def get_user_movies(self, user_id):
        """Get user-specific movies (not supported in file mode)."""
        raise NotImplementedError("User-specific movies not supported in FileDataManager.")

    # endregion

    # region CREATE
    def add_movie(self, data, id_column, **kwargs):
        """Add a new movie to the data dictionary and file."""
        if id_column and id_column in kwargs:
            id_column_val = kwargs.get(id_column)
            del kwargs[id_column]
        else:
            id_column_val = str(len(data) + 1)

        data[id_column_val] = kwargs
        self.write_data(data)
        return data

    # endregion

    # region UPDATE
    def write_data(self, data):
        """Write data back to the file."""
        self.__file_handler.write_data(data)

    def update_movie(self, data, unique_key, **kwargs):
        """Update an existing movie's data in the dictionary and file."""
        item = {**kwargs}
        item_key = DataUtils.data_key_by_kv(data, unique_key, item[unique_key])
        for key, value in kwargs.items():
            data[item_key][key] = value
        self.__file_handler.write_data(data)
        return data

    # endregion

    # region DELETE
    def delete_movie(self, data, key, value):
        """Delete a movie from the data dictionary and file."""
        item_key = DataUtils.data_key_by_kv(data, key, value)
        del data[item_key]
        self.__file_handler.write_data(data)
        return data
    # endregion
