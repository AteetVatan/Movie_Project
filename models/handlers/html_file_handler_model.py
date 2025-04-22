"""The HTML File operations module."""
import os
from config import config
from .file_handler_model import FileHandlerModel


class HtmlFileHandlerModel(FileHandlerModel):
    """Class responsible for HTML file operations."""
    __template_file_name = config.HTML_TEMPLATE_FILE
    __template_file_path = os.path.join(os.getcwd(), config.HTML_DIRECTORY, __template_file_name)
    __file_name = config.HTML_FILE
    __file_path = os.path.join(os.getcwd(), config.HTML_DIRECTORY, __file_name)
    __html_template = ""

    def __init__(self):
        if not os.path.exists(self.__template_file_path):  # Check if a Template file exists
            raise ValueError(f"HTML Template File Missing - {self.__file_path}")
        super().__init__(self.__file_path)
        self.__html_template = self.read_template_data()

    @property
    def html_template_data(self):
        """The HTML Template Data."""
        return self.__html_template

    @property
    def html_file_name(self):
        """The HTML File Name."""
        return self.__file_name

    @property
    def html_file_path(self):
        """The HTML File path."""
        return self.__file_path

    def read_template_data(self):
        """Method to read HTML Template file data."""
        return self.read_data(self.__template_file_path)

    def read_data(self, file_path: str = None):
        """Method to read HTML file data."""
        d = None
        try:
            if not file_path:
                file_path = self.__template_file_path

            with open(file_path, mode="rt", encoding="utf-8") as file:
                d = file.read()
        except FileNotFoundError as f:
            print(f)
        except IOError as e:
            print("FileHandler.read_data - I/O error occurred: ", os.strerror(e.errno))
        return d

    def write_html_data(self, html_data):
        """Method to read HTML Template file data."""
        return self.write_data(html_data, self.__file_path)

    def write_data(self, data, file_path: str = None):
        """Method to write HTML file data."""
        try:
            with open(file_path, mode="wt", encoding="utf-8") as file:
                file.write(data)
        except IOError as e:
            print("FileHandler.write_data - I/O error occurred: ", os.strerror(e.errno))
