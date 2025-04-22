"""The main Module."""
import argparse
from config import config
from singletons import AppInstance, DbInstance
from scripts.seed_movies import seed_movies_json_to_db
from constants import ConstantStrings
from helpers import PrintInputHelper as bp
from helpers import FileHelpers
from movie_app import MovieApp
from models.storage import StorageManager


def main():
    """The Main wrapper function."""

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
    if config.USE_DB_STORAGE:
        APP = AppInstance.get_app()
        DB = DbInstance.get_db()
        with APP.app_context():
            DB.create_all()
            seed_movies_json_to_db()
            main()
    else:
        main()
