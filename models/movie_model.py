"""The MovieModel Module."""
import random
import sys
from matplotlib import pyplot as plt
from models.html_file_handler_model import HtmlFileHandlerModel
from models.managers import DataManager
from models.base_model import BaseModel
from views import MovieView
from validation import MovieValidationManager as Mv
from helpers import DataHelpers
from enumerations import FileTypes, OMDBApiParamTypes
from constants.odmb_constants import OmdbConstants
from constants import DataConstants as Dc, ConstantStrings as Cs


class MovieModel(BaseModel):
    """The MovieModel Class."""

    def __init__(self, file_path, file_type=FileTypes.JSON):
        self.data = None
        super().__init__(file_path, file_type)
        self.__html_file_handler = HtmlFileHandlerModel()

    # region CREATE
    def add_data(self, **kwargs):
        """Adds a new movie to the data."""
        try:
            # use api to get year and rating for title
            title = kwargs.get("title")
            search_result = self.api_handler.get_data(title, OMDBApiParamTypes.TITLE)
            movie_found = OmdbConstants.item_found(search_result)
            id_column = OmdbConstants.get_data_constant_key(OmdbConstants.id())

            if movie_found:
                imdb_id = search_result.get(OmdbConstants.id())
                title = search_result.get(OmdbConstants.title())
                rating = search_result.get(OmdbConstants.rating())
                year = search_result.get(OmdbConstants.year())
                poster = search_result.get(OmdbConstants.poster())
                country = search_result.get(OmdbConstants.country())

                try:
                    rating = float(rating)
                except ValueError:
                    rating = "N/A"
                try:
                    year = int(year)
                except ValueError:
                    year = "N/A"

                self.data = DataManager.base_add_data_operation(self.data,
                                                                id_column=id_column,
                                                                id=imdb_id,
                                                                title=title,
                                                                rating=rating,
                                                                year=year,
                                                                poster=poster,
                                                                country=country)
                MovieView.data_added(new_movie=title)
            else:
                raise ValueError(f"Movie [{title}] not found in IMDB.")
        except ValueError as e:
            raise e

    def add_data_valid_movie(self, movie_name):
        """Method to validate the existing movie name."""
        try:
            Mv.movie_name_validation(movie_name=movie_name)
            movie_already_exists = (movie_name.lower()
                                    in DataManager.data_by_key(self.data, Dc.title()))
            if movie_already_exists:
                raise ValueError(Cs.MOVIE_EXIST)
        except ValueError as e:
            raise e

    # endregion CREATE

    # region READ
    def list_data(self):
        """Prints the Movies data in a list."""
        MovieView.movie_list_data(self.data)

    def show_random_item_in_data(self):
        """Prints random Movies."""
        random_key = random.choice(list(self.data.keys()))
        random_movie_data = self.data[random_key]
        MovieView.random_movie(random_movie_data=random_movie_data)

    def search_data(self, search_text: str):
        """method to search Movies."""
        try:
            search_text = search_text.lower()
            movie_rating_list = DataManager.data_by_keys(self.data, Dc.title(), Dc.rating())
            # normal search
            result_found = [x for x in movie_rating_list if search_text in x[0]]

            if len(result_found) <= 0:  # fuzzy search
                result_found = list(DataHelpers.fuzzy_string_matching(
                    movie_rating_list, search_text))
                if len(result_found) > 0:  # after fuzzy search
                    MovieView.movie_msg(Cs.MOVIE_SEARCH_MSG.format(KEY1=search_text))
                    MovieView.display_search_data(result_found)
                    return
                raise ValueError(Cs.MOVIE_SEARCH_ERROR.format(KEY1=search_text))
            MovieView.display_search_data(result_found)
        except ValueError as e:
            raise e

    def sort_data(self, key, reverse=False):
        """Method to sort the data.
        :param key: Given key to sort
        :param reverse: Acending or desciending
        :return:
        """
        movie_rating_list = DataManager.data_by_keys(self.data, Dc.title(), key)
        # Remove rating with N/A
        movie_rating_list = [x for x in movie_rating_list if isinstance(x[1], (int, float))]
        sorted_list = sorted(movie_rating_list, key=lambda x: x[1], reverse=reverse)
        MovieView.display_sorted_data(sorted_list)

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

            movie_rating_year_list = DataManager.data_by_keys(self.data,
                                                              Dc.title(),
                                                              Dc.rating(),
                                                              Dc.year())

            movie_rating_year_list = [x for x in movie_rating_year_list
                                      if isinstance(x[1], (int, float))]

            filtered_data = list(filter(lambda item1:
                                        all(x(item1) for x in dynamic_filter_dict.values()),
                                        movie_rating_year_list))
            if len(filtered_data) == 0:
                MovieView.movie_error(Cs.MOVIE_FILTER_NO_RESULT)
            else:
                MovieView.display_filtered_data(filtered_data)
        except ValueError as e:
            raise e

    def data_stats(self):
        """
        Method to print movie data statistic
        (average rating, median rating, the best movies and worst movies).
        """
        try:

            rating_data = DataManager.data_by_key(self.data, Dc.rating())
            # Making sure all entries must be number
            # some rating value can be 'N/A'
            rating_data = [x for x in rating_data if isinstance(x, (int, float))]
            avg_rating = sum(rating_data) / len(rating_data)
            median_rating = DataHelpers.find_median(rating_data)
            best_movies = [x for x in self.data.values() if x[Dc.rating()] == max(rating_data)]
            worst_movies = [x for x in self.data.values() if x[Dc.rating()] == min(rating_data)]
            MovieView.display_data_stats(best_movies=best_movies,
                                         worst_movies=worst_movies,
                                         avg_rating=avg_rating,
                                         median_rating=median_rating)
        except ValueError as e:
            raise e

    def show_data_histogram(self):
        """Method to generate Movie data Histogram."""
        try:
            movies_rating_list = DataManager.data_by_keys(self.data, Dc.title(), Dc.rating())
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
            MovieView.generate_website(self.data, self.__html_file_handler)
        except ValueError as e:
            raise e

    # endregion READ

    # region UPDATE

    def update_data(self, **kwargs):
        """Method to Update existing Movie."""
        try:
            self.data = DataManager.base_update_data_operation(self.data,
                                                               Dc.title(),
                                                               **kwargs)
            MovieView.update_movie_complete(update_movie_name=kwargs.get(Dc.title(), ""))
        except ValueError as e:
            raise e

    def update_data_valid_movie_name(self, update_movie_name):
        """Method to validate the existing movie name."""
        try:
            Mv.movie_name_validation(movie_name=update_movie_name)
            movie_exist = (update_movie_name.lower()
                           in DataManager.data_by_key(self.data, Dc.title()))
            if not movie_exist:
                raise ValueError(Cs.MOVIE_NOT_EXIST.format(KEY1=update_movie_name))
        except ValueError as e:
            raise e

    def save_data(self) -> bool:
        """Method to save movie."""
        try:
            self.file_handler.write_data(self.data)
            MovieView.save_movie_data_complete()
        except ValueError as e:
            raise e

    # endregion UPDATE

    # region DELETE
    def delete_data(self, title):
        """Method to delete the existing movie."""
        try:
            self.data = DataManager.base_delete_data_operation(self.data,
                                                               Dc.title(),
                                                               title)
            MovieView.movie_delete_complete(title=title)
        except ValueError as e:
            raise e

    def delete_data_valid(self, title):
        """Method to validate the existing movie name."""
        try:
            movie_exist = (title.lower()
                           in DataManager.data_by_key(self.data, Dc.title()))
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
        MovieView.movie_error(error)
    # endregion static-methods
