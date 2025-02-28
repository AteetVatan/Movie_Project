"""Module for Movie data CRUD methods."""
import os

from controllers.base_controller import BaseController
from validation import MovieValidationManager as Mv
from helpers import PrintInputHelper
from helpers.base_print_input_helper import PrintInputHelper as Ph
from constants import JsonConstants as Jc, ConstantStrings as Cs
from models import MovieModel
from models import MenuOperationOutputModel


class MoviesController(BaseController):
    """The Movie operations main class"""
    __data_desc = "movie"
    __file_name = "../data/movie.json"
    __file_path = os.path.join(os.getcwd(), "data", __file_name)

    def __init__(self):
        super().__init__(self.__data_desc)
        self.movie_model = MovieModel(self.__file_name, self.__file_path)

    # region CREATE
    def add_data(self):
        """Adds a new movie to the data."""
        try:
            # MOVIE_NAME
            while True:
                try:
                    new_movie = Ph.pr_input(Cs.NEW_MOVIE_NAME_ENTER)
                    if not new_movie:
                        return MenuOperationOutputModel(operation_wait=False)
                    self.movie_model.add_data_valid_movie(new_movie)
                    break
                except ValueError as e:
                    self.movie_model.movie_model_error(e.args[0])

            # MOVIE_YEAR
            while True:
                try:
                    year = Ph.pr_input(Cs.MOVIE_YEAR_ENTER)
                    if not year:
                        return MenuOperationOutputModel(operation_wait=False)
                    MovieModel.valid_movie_year(year)
                    break
                except ValueError as e:
                    self.movie_model.movie_model_error(e.args[0])

            # MOVIE_RATING
            while True:
                try:
                    rating = Ph.pr_input(Cs.MOVIE_RATING_ENTER)
                    if not rating:
                        return MenuOperationOutputModel(operation_wait=False)
                    MovieModel.valid_rating(rating)
                    break
                except ValueError as e:
                    self.movie_model.movie_model_error(e.args[0])

            self.movie_model.add_data(movie=new_movie, year=year, rating=rating)
        except ValueError as e:
            self.movie_model.movie_model_error(e.args[0])
        return MenuOperationOutputModel()

    # endregion CREATE

    # region READ
    def list_data(self):
        """Prints the Movies data in a list."""
        self.movie_model.list_data()
        return MenuOperationOutputModel()

    def show_random_item_in_data(self):
        """Prints random Movies."""
        self.movie_model.show_random_item_in_data()
        return MenuOperationOutputModel()

    def search_data(self):
        """method to search Movies."""
        while True:
            try:
                search_text = Ph.pr_input(Cs.MOVIE_NAME_PART)
                if search_text == "":
                    return MenuOperationOutputModel(operation_wait=False)
                self.movie_model.search_data(search_text)
                break
            except ValueError as e:
                self.movie_model.movie_model_error(e.args[0])
        return MenuOperationOutputModel()

    def sort_data(self, key, reverse=False):
        """Method to sort the data.
        :param key: Given key to sort
        :param reverse: Ascending or descending
        :return:
        """
        while True:
            try:
                if key == Jc.release_year():
                    usr_input = Ph.pr_input(Cs.MOVIE_SORT_YEAR_PROMPT).lower()
                    if usr_input == "":
                        return MenuOperationOutputModel(operation_wait=False)

                    if usr_input in ["y", "n"]:
                        reverse = usr_input == "y"
                    else:
                        raise ValueError(Cs.MOVIE_SORT_YEAR_PROMPT_ERROR)

                self.movie_model.sort_data(key, reverse)
                break
            except ValueError as e:
                self.movie_model.movie_model_error(e.args[0])
        return MenuOperationOutputModel()

    def data_filter(self):
        """Method the filter the movie data by ratings, start year and end year."""
        while True:
            try:
                filter_list = [{"key": "rating", "text": Cs.MOVIE_FILTER_RATING,
                                "validation": Mv.rating_validation},
                               {"key": "start_year", "text": Cs.MOVIE_FILTER_START_YEAR,
                                "validation": Mv.year_validation},
                               {"key": "end_year", "text": Cs.MOVIE_FILTER_END_YEAR,
                                "validation": Mv.year_validation},
                               ]

                filter_dict = self.__get_data_filter_dictionary(filter_list)
                self.movie_model.data_filter(filter_dict["rating"],
                                             filter_dict["start_year"],
                                             filter_dict["end_year"])

                break
            except ValueError as e:
                self.movie_model.movie_model_error(e.args[0])
        return MenuOperationOutputModel()

    def __get_data_filter_dictionary(self, filter_list):
        """Method creates the dictionary from given filter_list."""
        filter_dict = {}
        for filter_item in filter_list:
            while True:
                try:
                    v = Ph.pr_input(filter_item["text"])
                    if not v:
                        v = ""
                    else:
                        filter_item["validation"](v)
                    break
                except ValueError as e:
                    self.movie_model.movie_model_error(e.args[0])
            filter_dict[filter_item["key"]] = v

        return filter_dict

    def data_stats(self):
        """
        Method to print movie data statistic
        (average rating, median rating, the best movies and worst movies).
        """
        try:
            self.movie_model.data_stats()
        except ValueError as e:
            self.movie_model.movie_model_error(e.args[0])
        return MenuOperationOutputModel()

    def show_data_histogram(self):
        """Method to generate Movie data Histogram."""
        try:
            self.movie_model.show_data_histogram()
        except ValueError as e:
            self.movie_model.movie_model_error(e.args[0])
        return MenuOperationOutputModel()

    # endregion READ

    # region UPDATE
    def update_data(self):
        """Method to Update existing Movie."""
        while True:
            try:
                update_movie_name = Ph.pr_input(Cs.MOVIE_NAME_UPDATE)
                if not update_movie_name:
                    return MenuOperationOutputModel(operation_wait=False)
                self.movie_model.update_data_valid_movie(update_movie_name)
                break
            except ValueError as e:
                self.movie_model.movie_model_error(e.args[0])

        while True:
            try:
                rating = Ph.pr_input(Cs.MOVIE_RATING_ENTER)
                if not rating:
                    return MenuOperationOutputModel(operation_wait=False)
                MovieModel.valid_rating(rating)
                break
            except ValueError as e:
                self.movie_model.movie_model_error(e.args[0])

        try:
            self.movie_model.update_data(update_movie_name=update_movie_name, rating=rating)
        except ValueError as e:
            self.movie_model.movie_model_error(e.args[0])

        return MenuOperationOutputModel()

    def save_data(self):
        """Method to save movie."""
        try:
            self.movie_model.save_data()
        except ValueError as e:
            self.movie_model.movie_model_error(e.args[0])
        return MenuOperationOutputModel()

    # endregion UPDATE

    # region DELETE
    def delete_data(self):
        """Method to delete the existing movie."""
        while True:
            try:
                del_movie = Ph.pr_input(Cs.MOVIE_DELETE)
                if not del_movie:
                    return MenuOperationOutputModel(operation_wait=False)
                self.movie_model.delete_data(del_movie)
                break
            except ValueError as e:
                self.movie_model.movie_model_error(e.args[0])

        return MenuOperationOutputModel()

    # endregion DELETE

    # region EXIT

    def exit(self):
        """Exit Method."""
        PrintInputHelper.pr_bold("Bye!")
        return MenuOperationOutputModel(operation_exit=True)

    # endregion EXIT
