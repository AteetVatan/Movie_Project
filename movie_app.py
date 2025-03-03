from models.storage import StorageManager, IStorage


class MovieApp:
    def __init__(self, storage: IStorage):
        self._storage = storage

        # menu_controller = MenuController(AppTypes.MOVIE)
        # menu_controller.start()


    def _command_list_movies(self):
        movies = self._storage.list_movies()
        pass

    def _command_movie_stats(self):
        pass

    def _generate_website(self):
        pass

    def run(self):
        self._storage.menu_controller.start()