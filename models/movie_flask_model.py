"""The MovieModel Module."""
import random
import sys
from flask import jsonify
from matplotlib import pyplot as plt
from models.handlers import HtmlFileHandlerModel
from models.utils import DataUtils
from models.managers import FileDataManager
from models.managers import SQLAlchemyDataManager
from models.base_model import BaseModel
from views import MovieCliView, MovieFlaskView
from validation import MovieValidationManager as Mv
from helpers import DataHelpers
from enumerations import FileTypes, OMDBApiParamTypes
from constants.odmb_constants import OmdbConstants
from constants import DataConstants as Dc, ConstantStrings as Cs
from config import config


class MovieFlaskModel(BaseModel):
    """The MovieFlaskModel Class."""

    def __init__(self, file_path="", file_type=FileTypes.JSON):
        self.data = None

        if config.USE_DB_STORAGE:
            self.data_manager = SQLAlchemyDataManager()
        else:
            self.data_manager = FileDataManager(file_path, file_type)

        super().__init__(self.data_manager)

        for x in self.data:
            self.data[x][Dc.id()] = x

        self.view = MovieFlaskView()
        self.__html_file_handler = HtmlFileHandlerModel()

    def get_all_movies(self):
        """Method to get all Movies"""
        return self.data_manager.get_all_movies(self.data)

    def get_all_users(self):
        """Get all users from the database."""
        return self.data_manager.get_all_users()

    def get_user_by_id(self, user_id):
        """Get user by ID from a database."""
        return self.data_manager.get_user_by_id(user_id)

    def get_user_movies(self, user_id):
        """Get all movies for a specific user."""
        return self.data_manager.get_user_movies(user_id)

    def add_user(self, name):
        """Add a new user to the database."""
        return self.data_manager.add_user(name)

    def add_movie_to_user(self, user_id, movie):
        """Add a movie to user's favorites."""
        # modify current data
        movie_id = movie.get(Dc.imdb_id())
        if self.data.get(movie_id) is None:
            # Movie isn't found, add it to self.data
            self.data[movie_id] = movie
        return self.data_manager.add_movie_to_user(user_id, movie_id, movie)

    def update_data(self, movie_id, **kwargs):
        """Update movie details."""
        try:
            self.data = self.data_manager.update_movie(self.data, movie_id, **kwargs)
            return True
        except ValueError:
            return False

    def remove_movie_from_user(self, user_id, movie_id):
        """Remove a movie from user's favorites."""

        try:
            if self.data.get(movie_id) is None:
                return False

            self.data.pop(movie_id)
            self.data_manager.remove_movie_from_user(user_id, movie_id)
            return True
        except ValueError:
            return False

    # region CREATE
    def get_imdb_data(self, **kwargs):
        """Adds a new movie to the data."""
        try:
            # use api to get year and rating for title
            title = kwargs.get("title")
            search_result = self.api_handler.get_data(title, OMDBApiParamTypes.TITLE)
            movie_found = OmdbConstants.item_found(search_result)
            # id_column = OmdbConstants.get_data_constant_key(OmdbConstants.id())

            if movie_found:
                imdb_id = search_result.get(OmdbConstants.id())
                title = search_result.get(OmdbConstants.title())
                rating = search_result.get(OmdbConstants.rating())
                year = search_result.get(OmdbConstants.year())
                poster = search_result.get(OmdbConstants.poster())
                country = search_result.get(OmdbConstants.country()).split(", ")
                director = search_result.get(OmdbConstants.director())
                actors = search_result.get(OmdbConstants.actors()).split(", ")
                writer = search_result.get(OmdbConstants.writer()).split(", ")
                genre = search_result.get(OmdbConstants.genre()).split(", ")
                plot = search_result.get(OmdbConstants.plot())
                language = search_result.get(OmdbConstants.language())
                awards = search_result.get(OmdbConstants.awards()).split(", ")

                try:
                    rating = float(rating)
                except ValueError:
                    rating = "N/A"
                try:
                    year = int(year)
                except ValueError:
                    year = "N/A"

                return jsonify({
                    'success': True,
                    'movie': {
                        Dc.imdb_id(): imdb_id,
                        Dc.title(): title,
                        Dc.rating(): rating,
                        Dc.year(): year,
                        Dc.poster(): poster,
                        Dc.country(): country,
                        Dc.director(): director,
                        Dc.actors(): actors,
                        Dc.writer(): writer,
                        Dc.genre(): genre,
                        Dc.plot(): plot,
                        Dc.language(): language,
                        Dc.awards(): awards
                    }
                })

            return jsonify({
                'success': False,
                'error': f"Movie [{title}] not found in IMDB."
            })
        except ValueError as e:
            raise e

    def add_data_valid_movie(self, movie_name):
        """Method to validate the existing movie name."""
        try:
            Mv.movie_name_validation(movie_name=movie_name)
            movie_already_exists = (movie_name.lower()
                                    in DataUtils.data_by_key(self.data, Dc.title()))
            if movie_already_exists:
                raise ValueError(Cs.MOVIE_EXIST)
        except ValueError as e:
            raise e

    # endregion CREATE

    # region READ
    def list_data(self):
        """Prints the Movies data in a list."""
        MovieCliView.movie_list_data(self.data)

    def show_random_item_in_data(self):
        """Prints random Movies."""
        random_key = random.choice(list(self.data.keys()))
        random_movie_data = self.data[random_key]
        MovieCliView.random_movie(random_movie_data=random_movie_data)

    def search_data(self, search_text: str):
        """method to search existing Movies."""
        try:
            search_text = search_text.lower()
            movie_id_list = DataUtils.data_by_keys(self.data, Dc.title(), Dc.id())
            # normal search
            result_found = [x for x in movie_id_list if search_text in x[0]]

            if len(result_found) <= 0:  # fuzzy search
                result_found = list(DataHelpers.fuzzy_string_matching(
                    movie_id_list, search_text))

            movie_data_list = []
            if len(result_found) > 0:
                for item in result_found:
                    movie_data = self.data[item[1]]
                    movie_data_list.append(movie_data)

            return movie_data_list
        except ValueError as e:
            raise e

    def get_movie_by_id(self, unique_id):
        """Get all movies from the database."""
        movie_data = self.data
        movie = [(k, v) for k, v in movie_data.items()
                 if k.strip().lower() == unique_id.strip().lower()]
        if len(movie) == 0:
            raise ValueError(Cs.MOVIE_NOT_EXIST.format(KEY1=unique_id))
        movie[0][1][Dc.id()] = movie[0][0]  # add the id to the movie data
        return movie[0][1]

    def get_movie_by_title(self, title):
        """Get all movies from the database."""
        # Transform movie dictionary into a list for template
        movie_data = self.data
        movie = [(k, v) for k, v in movie_data.items()
                 if v[Dc.title()].strip().lower() == title.strip().lower()]
        if len(movie) == 0:
            raise ValueError(Cs.MOVIE_NOT_EXIST.format(KEY1=title))

        movie[0][1][Dc.id()] = movie[0][0]  # add the id to the movie data
        return movie[0][1]

    def sort_data(self, key, reverse=False):
        """Method to sort the data.
        :param key: Given key to sort
        :param reverse: Acending or desciending
        :return:
        """
        id_key_list = DataUtils.data_by_keys(self.data, Dc.id(), key)
        # Remove rating with N/A
        if key == Dc.rating() or key == Dc.year():
            id_key_list = [x for x in id_key_list if isinstance(x[1], (int, float))]
        sorted_list = sorted(id_key_list, key=lambda x: x[1], reverse=reverse)

        movie_data_list = []
        for item in sorted_list:
            movie_data = self.data[item[0]]
            movie_data_list.append(movie_data)
        return movie_data_list

    def data_filter(self, rating, start_year, end_year):
        """Method the filter the movie data by ratings, start year and end year."""

        try:
            dynamic_filter_dict = {}
            if rating:
                Mv.rating_validation(rating)
                dynamic_filter_dict[0] = lambda x: x[1] >= float(rating)
            if start_year:
                Mv.year_validation(start_year)
                dynamic_filter_dict[1] = lambda x: x[2] >= int(start_year)
            if end_year:
                Mv.year_validation(end_year)
                dynamic_filter_dict[2] = lambda x: x[2] <= int(end_year)

            movie_rating_year_list = DataUtils.data_by_keys(self.data,
                                                            Dc.title(),
                                                            Dc.rating(),
                                                            Dc.year())

            movie_rating_year_list = [x for x in movie_rating_year_list
                                      if isinstance(x[1], (int, float))]

            filtered_data = list(filter(lambda item1:
                                        all(x(item1) for x in dynamic_filter_dict.values()),
                                        movie_rating_year_list))
            if len(filtered_data) == 0:
                MovieCliView.movie_error(Cs.MOVIE_FILTER_NO_RESULT)
            else:
                MovieCliView.display_filtered_data(filtered_data)
        except ValueError as e:
            raise e

    def data_stats(self):
        """
        Method to print movie data statistic
        (average rating, median rating, the best movies and worst movies).
        """
        try:

            rating_data = DataUtils.data_by_key(self.data, Dc.rating())
            # Making sure all entries must be number
            # some rating value can be 'N/A'
            rating_data = [x for x in rating_data if isinstance(x, (int, float))]
            avg_rating = sum(rating_data) / len(rating_data)
            median_rating = DataHelpers.find_median(rating_data)
            best_movies = [x for x in self.data.values() if x[Dc.rating()] == max(rating_data)]
            worst_movies = [x for x in self.data.values() if x[Dc.rating()] == min(rating_data)]
            MovieCliView.display_data_stats(best_movies=best_movies,
                                            worst_movies=worst_movies,
                                            avg_rating=avg_rating,
                                            median_rating=median_rating)
        except ValueError as e:
            raise e

    def show_data_histogram(self):
        """Method to generate Movie data Histogram."""
        try:
            movies_rating_list = DataUtils.data_by_keys(self.data, Dc.title(), Dc.rating())
            plt.hist(movies_rating_list, edgecolor="black")
            plt.title(Cs.MOVIE_HISTOGRAM)
            plt.ylabel(Cs.MOVIE_FREQUENCY)
            plt.xlabel(Cs.MOVIE_RATING)
            plt.show()
            # Two lines to make our compiler able to draw:
            plt.savefig(sys.stdout.buffer)
            sys.stdout.flush()
        except ValueError as e:
            raise e

    def generate_website(self):
        """Method to generate_website."""
        try:
            MovieCliView.generate_website(self.data, self.__html_file_handler)
        except ValueError as e:
            raise e

    # endregion READ

    # region UPDATE

    def save_data(self) -> bool:
        """Method to save movie."""
        try:
            self.data_manager.write_data(self.data)
            MovieCliView.save_movie_data_complete()
        except ValueError as e:
            raise e

    # endregion UPDATE

    # region DELETE
    def delete_data(self, title):
        """Method to delete the existing movie."""
        try:
            self.data = self.data_manager.delete_movie(self.data,
                                                       Dc.title(),
                                                       title)
            MovieCliView.movie_delete_complete(title=title)
        except ValueError as e:
            raise e

    def delete_data_valid(self, title):
        """Method to validate the existing movie name."""
        try:
            movie_exist = (title.lower()
                           in DataUtils.data_by_key(self.data, Dc.title()))
            if not movie_exist:
                raise ValueError(Cs.MOVIE_NOT_EXIST.format(KEY1=title))
        except ValueError as e:
            raise e

    # endregion DELETE

    # region static-methods
    @staticmethod
    def valid_movie_year(year):
        """Method to validate the existing movie name."""
        Mv.year_validation(year)

    @staticmethod
    def valid_rating(rating):
        """Method to validate the movie rating."""
        Mv.rating_validation(rating)

    @staticmethod
    def movie_model_error(error):
        """Method for Movie Modal Errors."""
        MovieCliView.movie_error(error)

    # endregion static-methods

    def get_movie_object_from_json(self, imdb_id, movie_data):
        """Method to get the movie object from the json data."""
        return self.data_manager.get_movie_object_from_json(imdb_id, movie_data)
