"""Module for Movie data CRUD methods."""
import random
import sys
import matplotlib.pyplot as plt
from base.base_controller import BaseController
from base.movie_validation_manager import MovieValidationManager as Mv
from constants.json_constants import JsonConstants as Jc
from helpers.movie_print import MoviePrint as Mp, MoviePrintEnum as Me
from data.data_handler import DataHandler


class MoviesController(BaseController):
    """The Movie operations main class"""
    __data_desc = "movie"

    def __init__(self, movies):
        super().__init__(movies, self.__data_desc)

    # region CREATE
    def add_data(self):
        """Adds a new movie to the data."""
        try:
            new_movie = Mp.pr_input(Mp.get_prompt_string(Me.NEW_MOVIE_NAME.value))
            valid_movie = (new_movie.lower() not in self.data_manager.data_by_key(Jc.title()))
            if not valid_movie:
                Mp.pr_error(Mp.get_prompt_string(Me.MOVIE_EXIST.value))
                return
            year = Mp.pr_input(Mp.get_prompt_string(Me.MOVIE_YEAR.value))
            if not Mv.year_validation(year):
                return
            rating = Mp.pr_input(Mp.get_prompt_string(Me.MOVIE_RATING_ENTER.value))
            if not Mv.rating_validation(rating):
                return
            self.data_manager.base_add_data_operation(title=new_movie,
                                                      rating=float(rating), release_year=int(year))
            Mp.pr_menu(Mp.get_prompt_string(Me.MOVIE_ADDED.value, KEY1=new_movie))
        except ValueError:
            Mp.pr_error(Mp.get_prompt_string(Me.MOVIE_VALUE_ERROR.value))

    # endregion CREATE

    # region READ
    def list_data(self):
        """Prints the Movies data in a list."""
        movie_length = len(self.data) + 1
        Mp.pr_menu(Mp.get_prompt_string(Me.MOVIE_TOTAL.value, KEY1=movie_length))
        for item in self.data.values():
            Mp.pr_menu(f"{item[Jc.title()]} ({item[Jc.release_year()]}): {item[Jc.rating()]}")
        return False

    def show_random_item_in_data(self):
        """Prints random Movies."""
        random_index = random.randint(1, len(self.data))
        random_movie_data = self.data[str(random_index)]
        Mp.pr_menu(
            Mp.get_prompt_string(Me.MOVIE_CHOSEN.value, KEY1=random_movie_data[Jc.title()],
                                 KEY2=random_movie_data[Jc.rating()]))
        return False

    def search_data(self):
        """Method to search Movies."""
        search_text = str(Mp.pr_input(Mp.get_prompt_string(Me.MOVIE_NAME_PART.value)))
        search_text = search_text.lower().strip()

        if search_text == "":
            return False

        movie_rating_list = self.data_manager.data_by_keys(Jc.title(), Jc.rating())
        # normal search
        result_found = [x for x in movie_rating_list if search_text in x[0]]

        if len(result_found) <= 0:  # fuzzy search
            result_found = list(MoviesController.__fuzzy_string_matching(
                movie_rating_list, search_text))
            if len(result_found) > 0:  # after fuzzy search
                Mp.pr_error(Mp.get_prompt_string(Me.MOVIE_SEARCH_MSG.value, KEY1=search_text))

        for item in result_found:
            Mp.pr_menu(f"{item[0].title()}, {item[1]}")
        return False

    def sort_data(self, key, reverse=False):
        """Method to sort the data.
        :param key: Given key to sort
        :param reverse: Acending or desciending
        :return:
        """
        movie_rating_list = self.data_manager.data_by_keys(Jc.title(), key)
        if key == Jc.release_year():
            reverse = MoviesController.__get_sort_order_year_data()

        sorted_list = sorted(movie_rating_list, key=lambda x: x[1], reverse=reverse)
        for item in sorted_list:
            Mp.pr_menu(f"{item[0]}: {item[1]}")
        return False

    def data_filter(self) -> bool:
        """Method the filter the movie data by ratings, start year and end year."""
        movie_rating_year_list = self.data_manager.data_by_keys(Jc.title(),
                                                                Jc.rating(), Jc.release_year())
        rating = Mp.pr_input(Mp.get_prompt_string(Me.MOVIE_FILTER_RATING.value)).strip()
        start_year = Mp.pr_input(Mp.get_prompt_string(Me.MOVIE_FILTER_START_YEAR.value)).strip()
        end_year = Mp.pr_input(Mp.get_prompt_string(Me.MOVIE_FILTER_END_YEAR.value)).strip()

        if not Mv.rating_validation(rating) or not Mv.year_validation(
                start_year) or not Mv.year_validation(
            end_year):
            return False

        dynamic_filter_dict = {}
        if rating:
            dynamic_filter_dict[0] = lambda x: x[1] >= float(rating)
        if start_year:
            dynamic_filter_dict[1] = lambda x: x[2] >= int(start_year)
        if end_year:
            dynamic_filter_dict[2] = lambda x: x[2] <= int(end_year)

        filtered_data = list(filter(lambda item1:
                                    all(x(item1) for x in dynamic_filter_dict.values()),
                                    movie_rating_year_list))

        if len(filtered_data) == 0:
            Mp.pr_error(Mp.get_prompt_string(Me.MOVIE_FILTER_NO_RESULT.value))
        for item in filtered_data:
            Mp.pr_menu(f"{item[0]} ({item[2]}): {item[1]}")

        return False

    def data_stats(self):
        """
        Method to print movie data statistic
        (average rating, median rating, the best movies and worst movies).
        """
        try:
            rating_data = self.data_manager.data_by_key(Jc.rating())
            # Making sure all entries must be number
            rating_data = [float(x) for x in rating_data]
            avg_rating = sum(rating_data) / len(rating_data)
            median_rating = MoviesController.__find_median(rating_data)
            best_movies = [x for x in self.data.values() if x[Jc.rating()] == max(rating_data)]
            worst_movies = [x for x in self.data.values() if x[Jc.rating()] == min(rating_data)]
            Mp.pr_menu(Mp.get_prompt_string(Me.AVG_RATING.value, KEY1=avg_rating))
            Mp.pr_menu(Mp.get_prompt_string(Me.MEDIAN_RATING.value, KEY1=median_rating))
            for item in best_movies:
                Mp.pr_menu(Mp.get_prompt_string(Me.MOVIE_BEST.value,
                                                KEY1=item[Jc.title()], KEY2=item[Jc.rating()]))
            for item in worst_movies:
                Mp.pr_menu(Mp.get_prompt_string(Me.MOVIE_WORST.value,
                                                KEY1=item[Jc.title()], KEY2=item[Jc.rating()]))
        except ValueError as e:
            print(e)

    def show_data_histogram(self):
        """Method to generate Movie data Histogram."""
        movies_rating_list = self.data_manager.data_by_keys(Jc.title(), Jc.rating())
        plt.hist(movies_rating_list, edgecolor="black")
        plt.title(Mp.get_prompt_string(Me.MOVIE_HISTOGRAM.value))
        plt.ylabel(Mp.get_prompt_string(Me.MOVIE_FREQUENCY.value))
        plt.xlabel(Mp.get_prompt_string(Me.MOVIE_RATING.value))
        plt.show()
        # Two  lines to make our compiler able to draw:
        plt.savefig(sys.stdout.buffer)
        sys.stdout.flush()
        return False

    # endregion READ

    # region UPDATE
    def update_data(self):
        """Method to Update existing Movie."""
        update_movie_name = Mp.pr_input(Mp.get_prompt_string(Me.MOVIE_NAME.value))
        valid_movie = (update_movie_name.lower() in self.data_manager.data_by_key(Jc.title()))
        if not valid_movie:
            Mp.pr_error(Mp.get_prompt_string(Me.MOVIE_EXIST.value))
            return False

        rating = Mp.pr_input(Mp.get_prompt_string(Me.MOVIE_RATING_ENTER.value))

        if not Mv.rating_validation(rating):
            return False

        self.data_manager.base_update_data_operation(Jc.title(),
                                                     title=update_movie_name, rating=float(rating))
        Mp.pr_menu(Mp.get_prompt_string(Me.MOVIE_UPDATED.value, KEY1=update_movie_name))
        return False

    def save_data(self) -> bool:
        """Method to save movie."""
        DataHandler.write_data(self.data)
        Mp.pr_menu(Mp.get_prompt_string(Me.MOVIE_DATA_SAVED.value))
        return False
    # endregion UPDATE

    # region DELETE
    def delete_item_in_data(self):
        """Method to delete the existing movie."""
        del_movie = Mp.pr_input(Mp.get_prompt_string(Me.MOVIE_DELETE.value))

        if del_movie in self.data_manager.data_by_key(Jc.title()):
            self.data_manager.base_delete_data_operation(Jc.title(), del_movie)
            Mp.pr_menu(Mp.get_prompt_string(Me.MOVIE_DELETE_DONE.value, KEY1=del_movie))
        else:
            Mp.pr_error(Mp.get_prompt_string(Me.MOVIE_NOT_EXIST.value, KEY1=del_movie))
        return False

    # endregion DELETE

    # region EXIT

    def exit(self):
        """Exit Method."""
        print("Bye!")
        return True

    # endregion EXIT
    # region Private static Methods

    @staticmethod
    def __get_sort_order_year_data():
        """Method to sort the data."""
        while True:
            usr_input = Mp.pr_input(Mp.get_prompt_string(Me.MOVIE_SORT_YEAR_PROMPT.value)).lower()
            if usr_input in ["y", "n"]:
                return usr_input == "y"
            Mp.pr_error(Mp.get_prompt_string(Me.MOVIE_SORT_YEAR_PROMPT_ERROR.value))

    @staticmethod
    def __find_median(values: list) -> float:
        """Method to find ratings data median."""
        length = len(values)
        if length % 2 == 0:  # Even
            index = int(length / 2)
            return (values[index - 1] + values[index]) / 2
        index = length // 2
        return values[index]

    @staticmethod
    def __fuzzy_string_matching(movie_rating_list: list, search_text: str) -> list:
        """Method to find fuzzy strings matches."""
        distance_dict = {}
        for item in movie_rating_list:
            distance = MoviesController.__levenshtein_distance(search_text, item[0])
            distance_dict[item] = distance

        sorted_distance_key_list = sorted(distance_dict.items(), key=lambda x: x[1])
        sorted_movie_list = [x[0] for x in sorted_distance_key_list]
        if len(movie_rating_list) > 5:
            return sorted_movie_list[:6]
        return sorted_movie_list[:1]

    @staticmethod
    def __levenshtein_distance(a, b):
        """Method implementing levenshtein_distance Algorithm."""
        n, m = len(a), len(b)
        # Create an array of size NxM
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        # Base Case: When N = 0
        for j in range(m + 1):
            dp[0][j] = j
        # Base Case: When M = 0
        for i in range(n + 1):
            dp[i][0] = i
        # Transitions
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],  # Insertion
                        dp[i][j - 1],  # Deletion
                        dp[i - 1][j - 1]  # Replacement
                    )

        return dp[n][m]
    # endregion Private static Methods
