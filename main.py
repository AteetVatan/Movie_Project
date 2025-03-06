"""The main Module."""
import argparse

from constants import ConstantStrings
from helpers import PrintInputHelper as bp
from helpers import FileHelpers
from movie_app import MovieApp
from models.storage import StorageManager


def main():
    """The Main wrapper function."""
    # file_name = "data.json"

    bp.pr_menu(ConstantStrings.MAIN_PRINT_WELCOME)
    bp.pr_menu(ConstantStrings.MAIN_PRINT_INTRODUCTION)
    file_name = get_cmd_arguments()
    file_name = FileHelpers.file_correction(file_name)
    file_path = FileHelpers.get_data_file_path(file_name)
    storage_manager = StorageManager(file_path)
    storage = storage_manager.storage
    movie_app = MovieApp(storage)
    movie_app.run()


def get_cmd_arguments():
    """Method to get the command line argument which is the file name"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file_name",
        type=str,
        nargs="?",
        default="data.json",
        help="file name for storing data (default: data.json)",
    )
    args = parser.parse_args()
    return args.file_name


if __name__ == "__main__":
    main()
