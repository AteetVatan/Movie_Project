"""Module to create, read and write data"""
import csv
import os
from models import FileHandlerModel
from helpers import PrintInputHelper as Ph
from constants import ConstantStrings as Cs, DataConstants


class CsvFileHandlerModel(FileHandlerModel):
    """Class responsible for CSV file operations."""

    def __init__(self, file_path):
        # Set CSV Metadata
        (self.__csv_all_columns,
         self.__csv_attr_columns,
         self.csv_key_column) = self.__get_csv_metadata()

        if not os.path.exists(file_path):  # Check if a file exists
            self.write_data(data=None, file_path=file_path)
            # raise ValueError(Cs.FILE_NOT_EXIST.format(KEY=file_path))

        super().__init__(file_path)

    @property
    def csv_all_columns(self):
        """Property to get CSV columns headers."""
        # columns = ("index", "title", "year", "rating")
        return self.__csv_all_columns

    @property
    def csv_attribute_columns(self):
        """Property to get CSV columns headers."""
        # columns = ("index", "title", "year", "rating")
        return self.__csv_attr_columns

    @property
    def csv_key_column(self):
        """Property to get CSV unique columns."""
        return self.__csv_key_column

    @csv_key_column.setter
    def csv_key_column(self, value):
        try:
            # Ensure the key_column exists in csv_columns
            if value not in self.__csv_all_columns:
                raise ValueError(f"Key column '{value}' must be in {self.__csv_all_columns}")

            self.__csv_key_column = value
        except ValueError as e:
            Ph.pr_error(e.args[0])

    def read_data(self, file_path: str = None):
        """Method to read file data."""

        if not file_path:
            file_path = self.file_path

        read_dict = {}
        try:
            with open(file_path, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if self.csv_attribute_columns:
                        row_dict = {col: row[col] for col in self.csv_attribute_columns if col in row}
                    else:
                        row_dict = row

                    key = row.get(self.csv_key_column)
                    read_dict[key] = row_dict
        except ValueError as e:
            Ph.pr_error(e.args[0])
        except FileNotFoundError as f:
            Ph.pr_error(f)
        except IOError as e:
            Ph.pr_error("I/O error occurred: ", os.strerror(e.errno))
        return read_dict

    def write_data(self, data, file_path: str = None):
        """Method to write data to file"""
        try:
            if not file_path:
                file_path = self.file_path

            if data is None:
                data = {}

            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                # Header Row
                writer.writerow(self.csv_all_columns)

                for id_key, row_data in data.items():
                    row_list = [id_key]
                    # Add other column values
                    for column in self.csv_attribute_columns:
                        val = row_data.get(column)
                        if not val:
                            raise ValueError(f"Missing  {column}  in row: {row_data}")
                        row_list.append(val)

                    writer.writerow(row_list)
        except ValueError as e:
            Ph.pr_error(e.args[0])
        except FileNotFoundError as f:
            Ph.pr_error(f)
        except IOError as e:
            Ph.pr_error("I/O error occurred: ", os.strerror(e.errno))

    def __get_csv_metadata(self, file_path: str = None):
        """Method to read file data."""
        all_csv_headers = (DataConstants.id(),
                                DataConstants.title(),
                                DataConstants.year(),
                                DataConstants.rating(),
                                DataConstants.poster())
        csv_key_column = all_csv_headers[0]
        csv_attr_columns = all_csv_headers[1:]
        return all_csv_headers, csv_attr_columns, csv_key_column

        if not file_path:
            file_path = self.file_path
        try:
            with open(file_path, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    all_csv_headers = tuple(row.keys())
                    csv_key_column = all_csv_headers[0]
                    csv_attr_columns = all_csv_headers[1:]
                    break
        except ValueError as e:
            Ph.pr_error(e.args[0])
        except FileNotFoundError as f:
            Ph.pr_error(f)
        except IOError as e:
            Ph.pr_error("I/O error occurred: ", os.strerror(e.errno))
        return all_csv_headers, csv_attr_columns, csv_key_column
