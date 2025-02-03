"""Module for Movie Data Print strings."""
from enum import Enum
from helpers.base_print import BasePrint


class MoviePrintEnum(Enum):
    """Enumeration to define Print strings keys."""
    NEW_MOVIE_NAME = 0
    MOVIE_NAME = 1
    MOVIE_NAME_PART = 2
    MOVIE_EXIST = 3
    MOVIE_ADDED = 4
    MOVIE_DELETE = 5
    MOVIE_DELETE_DONE = 6
    MOVIE_NOT_EXIST = 7
    MOVIE_TOTAL = 8
    MOVIE_UPDATED = 9
    MOVIE_CHOSEN = 10
    MOVIE_SEARCH_MSG = 11
    MOVIE_RATING_ENTER = 12
    MOVIE_RATING_MSG = 13
    MOVIE_RATING = 14
    AVG_RATING = 15
    MEDIAN_RATING = 16
    MOVIE_BEST = 17
    MOVIE_WORST = 18
    MOVIE_HISTOGRAM = 19
    MOVIE_FREQUENCY = 20
    MOVIE_YEAR = 21
    MOVIE_VALUE_ERROR = 22
    MOVIE_SORT_YEAR_PROMPT = 23
    MOVIE_SORT_YEAR_PROMPT_ERROR = 24
    MOVIE_YEAR_PROMPT_ERROR = 25
    MOVIE_FILTER_RATING = 26
    MOVIE_FILTER_START_YEAR = 27
    MOVIE_FILTER_END_YEAR = 28
    MOVIE_FILTER_NO_RESULT = 29
    MOVIE_DATA_SAVED = 30

class MoviePrint(BasePrint):
    """Class containing Print strings."""
    _prompt_dictionary = {MoviePrintEnum.NEW_MOVIE_NAME.value:
                              'Enter new movie name: ',
                          MoviePrintEnum.MOVIE_NAME.value:
                              'Enter movie name: ',
                          MoviePrintEnum.MOVIE_NAME_PART.value:
                              'Enter part of movie name: ',
                          MoviePrintEnum.MOVIE_YEAR.value:
                              'Enter the movie year: ',
                          MoviePrintEnum.MOVIE_EXIST.value:
                              'Movie already exists.',
                          MoviePrintEnum.MOVIE_ADDED.value:
                              'Movie {KEY1} successfully added',
                          MoviePrintEnum.MOVIE_RATING_ENTER.value:
                              'Enter new movie rating (0-10): ',
                          MoviePrintEnum.MOVIE_RATING_MSG.value:
                              'Ratings must be between 1-10.',
                          MoviePrintEnum.MOVIE_TOTAL.value:
                              '{KEY1} movies in total',
                          MoviePrintEnum.MOVIE_UPDATED.value:
                              'Movie {KEY1} successfully updated: ',
                          MoviePrintEnum.MOVIE_CHOSEN.value:
                              "Your movie for tonight: {KEY1}, it's rated {KEY2}",
                          MoviePrintEnum.MOVIE_SEARCH_MSG.value:
                              'The movie "{KEY1}" does not exist. Did you mean: ',
                          MoviePrintEnum.MOVIE_RATING.value:
                              'Movie Ratings',
                          MoviePrintEnum.AVG_RATING.value:
                              'Average rating: {KEY1}',
                          MoviePrintEnum.MEDIAN_RATING.value:
                              'Median rating: {KEY1}',
                          MoviePrintEnum.MOVIE_BEST.value:
                              'Best movie: {KEY1}, {KEY2}',
                          MoviePrintEnum.MOVIE_WORST.value:
                              'Worst movie: {KEY1}, {KEY2}',
                          MoviePrintEnum.MOVIE_HISTOGRAM.value:
                              'Movie Histogram',
                          MoviePrintEnum.MOVIE_FREQUENCY.value:
                              'Movie Frequency',
                          MoviePrintEnum.MOVIE_DELETE.value:
                              'Enter movie name to delete: ',
                          MoviePrintEnum.MOVIE_DELETE_DONE.value:
                              'Movie {KEY1} successfully deleted',
                          MoviePrintEnum.MOVIE_NOT_EXIST.value:
                              "Movie {KEY1} doesn't exist!",
                          MoviePrintEnum.MOVIE_VALUE_ERROR.value:
                              'Please Enter Numeric Value',
                          MoviePrintEnum.MOVIE_SORT_YEAR_PROMPT.value:
                              'Do you want the latest movies first? (Y/N) ',
                          MoviePrintEnum.MOVIE_SORT_YEAR_PROMPT_ERROR.value:
                              'Please enter Y or N!',
                          MoviePrintEnum.MOVIE_YEAR_PROMPT_ERROR.value:
                              'Year must be between 1900 and {KEY1}',
                          MoviePrintEnum.MOVIE_FILTER_RATING.value:
                              'Enter minimum rating (leave blank for no minimum rating): ',
                          MoviePrintEnum.MOVIE_FILTER_START_YEAR.value:
                              'Enter start year (leave blank for no start year): ',
                          MoviePrintEnum.MOVIE_FILTER_END_YEAR.value:
                              'Enter end year (leave blank for no end year): ',
                          MoviePrintEnum.MOVIE_FILTER_NO_RESULT.value:
                              'No Movies found for this filter set.',
                          MoviePrintEnum.MOVIE_DATA_SAVED.value:
                              'Movie data successfully saved.'
                          }
