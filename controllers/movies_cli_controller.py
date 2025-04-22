"""Module for Movie data CRUD methods."""
import os

from config import config
from enumerations import FileTypes
from validation import MovieValidationManager as Mv
from helpers import PrintInputHelper
from helpers.base_print_input_helper import PrintInputHelper as Ph
from constants import DataConstants as Dc, ConstantStrings as Cs
from models import MovieCliModel
from models import MenuOperationOutputModel
from .base_controller import BaseController
from .menu_controller import MenuController


class MoviesCliController(BaseController):
    """The Movie operations main class"""
    __data_desc = "movie"
    __file_name = "../data/data.json"
    __file_path = os.path.join(os.getcwd(), config.DATA_DIRECTORY, __file_name)

    def __init__(self, file_path="", file_type=FileTypes.JSON):
        menu_items = MenuController.get_menu_dictionary(self, self.__data_desc)
        super().__init__(menu_items)
        if file_path:
            self.__file_path = file_path
        self.movie_model = MovieCliModel(self.__file_path, file_type)

    # region CREATE
    def add_data(self):
        """Adds a new movie to the data."""
        while True:
            try:
                input_dict = {
                    Dc.title(): {"prompt": Cs.NEW_MOVIE_NAME_ENTER,
                                 "validation": self.movie_model.add_data_valid_movie}}

                # Get user Inputs
                result = self.__get_console_user_inputs(input_dict)
                if isinstance(result, MenuOperationOutputModel):
                    return result
                title, = result
                self.movie_model.get_imdb_data(title=title)
                break
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
                if key == Dc.year():
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

    def generate_website(self):
        """Method to generate_website."""
        try:
            self.movie_model.generate_website()
        except ValueError as e:
            self.movie_model.movie_model_error(e.args[0])
        return MenuOperationOutputModel()

    # endregion READ

    # region UPDATE
    def update_data(self):
        """Method to Update existing Movie."""
        try:

            input_dict = {
                Dc.title(): {"prompt": Cs.MOVIE_NAME_UPDATE,
                             "validation": self.movie_model.update_data_valid_movie_name},
                Dc.notes(): {"prompt": Cs.MOVIE_NAME_UPDATE_NOTES, "validation": lambda x: True}}

            # Get user Inputs
            result = self.__get_console_user_inputs(input_dict)
            if isinstance(result, MenuOperationOutputModel):
                return result
            title, notes = result
            self.movie_model.update_data(title=title, notes=notes)
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
                input_dict = {
                    Dc.title(): {"prompt": Cs.MOVIE_DELETE,
                                 "validation": self.movie_model.delete_data_valid}}
                result = self.__get_console_user_inputs(input_dict)
                if isinstance(result, MenuOperationOutputModel):
                    return result
                title, = result
                self.movie_model.delete_data(title)
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

    # region Helper methods
    def __get_console_user_inputs(self, input_dict: dict):
        """Method to get user input from console."""
        # input_dict = {
        #     Dc.title(): {"prompt": Cs.NEW_MOVIE_NAME_ENTER,
        #                  "validation": self.movie_model.add_data_valid_movie},
        #     Dc.title(): {"prompt": Cs.NEW_MOVIE_NAME_ENTER,
        #                  "validation": self.movie_model.add_data_valid_movie},
        #     Dc.title(): {"prompt": Cs.NEW_MOVIE_NAME_ENTER,
        #                  "validation": self.movie_model.add_data_valid_movie}}

        result_list = []
        for user_input in input_dict.values():
            val = self.__get_valid_input(user_input["prompt"], user_input["validation"])
            if val is None:
                return MenuOperationOutputModel(operation_wait=False)
            result_list.append(val)

        return tuple(result_list)

    def __get_valid_input(self, prompt, validation_func):
        """Helper method to get and validate user input"""
        while True:
            try:
                user_input = Ph.pr_input(prompt)
                if not user_input:
                    return None  # Exit if input is empty
                validation_func(user_input)
                return user_input
            except ValueError as e:
                self.movie_model.movie_model_error(e.args[0])
    # endregion Helper methods
