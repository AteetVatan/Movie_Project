"""The main Module."""
import os
from movie_app import MovieApp
from models.storage import StorageManager


def main():
    """The Main wrapper function."""
    #file_name = "movie.json"
    file_name = "movie.csv"
    file_path = os.path.join(os.getcwd(), "data", file_name)
    storage_manager = StorageManager(file_path)
    storage = storage_manager.storage
    movie_app = MovieApp(storage)
    movie_app.run()


if __name__ == "__main__":
    main()
