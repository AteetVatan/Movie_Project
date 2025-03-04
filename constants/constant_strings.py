"""The String Constants Module."""


class ConstantStrings:
    """Class to define String Constants."""
    # Menu Constants
    MAIN_PRINT_WELCOME = '---------- Movies App ----------\n'
    MAIN_PRINT_ENTER_CHOICE = 'Enter choice (1-{key1}): '
    MAIN_PRINT_CONTINUE = 'Press enter for Menu.....'
    MAIN_PRINT_INVALID = 'Invalid Choice'
    MAIN_PRINT_MENU = 'Menu: '

    # Movie Constants
    NEW_MOVIE_NAME_ENTER = 'Enter new movie name [or empty text for Menu.]\n: '
    MOVIE_NAME_UPDATE = 'Enter movie name to be updated [or empty text for Menu.]\n: '
    MOVIE_NAME_PART = 'Enter part of movie name [or empty text for Menu.]\n: '
    MOVIE_NAME_ERROR = 'Enter a valid movie name.'
    MOVIE_EXIST = 'Movie already exists.'
    MOVIE_ADDED = 'Movie {KEY1} successfully added.'
    MOVIE_DELETE = 'Enter movie name to delete [or empty text for Menu.]\n: '
    MOVIE_DELETE_DONE = 'Movie {KEY1} successfully deleted'
    MOVIE_NOT_EXIST = "Movie {KEY1} doesn't exist!"
    MOVIE_TOTAL = '\t{KEY1} movies in total.'
    MOVIE_UPDATED = 'Movie {KEY1} successfully updated: '
    MOVIE_CHOSEN = "Your movie for tonight: {KEY1}, it's rated {KEY2}."
    MOVIE_SEARCH_MSG = 'The movie "{KEY1}" does not exist. Did you mean: '
    MOVIE_SEARCH_ERROR = 'The movie "{KEY1}" does not exist.'
    MOVIE_RATING_ENTER = 'Enter new movie rating (0-10) [or empty text for Menu.]\n: '
    MOVIE_RATING_MSG = 'Ratings must be between 1-10.'
    MOVIE_RATING_ERROR = 'Ratings must be a number.'
    MOVIE_RATING = 'Movie Ratings.'
    AVG_RATING = 'Average rating: {KEY1}'
    MEDIAN_RATING = 'Median rating: {KEY1}'
    MOVIE_BEST = 'Best movie: {KEY1}, {KEY2}'
    MOVIE_WORST = 'Worst movie: {KEY1}, {KEY2}'
    MOVIE_HISTOGRAM = 'Movie Histogram.'
    MOVIE_FREQUENCY = 'Movie Frequency.'
    MOVIE_YEAR_ENTER = 'Enter the movie year [or empty text for Menu.]\n: '
    MOVIE_VALUE_ERROR = 'Please Enter Numeric Value.'
    MOVIE_SORT_YEAR_PROMPT = ('Do you want the latest movies first? (Y/N) '
                              '[or empty text for Menu.]\n: ')
    MOVIE_SORT_YEAR_PROMPT_ERROR = 'Please enter Y or N!.'
    MOVIE_YEAR_PROMPT_ERROR = 'Year must be number between 1900 and {KEY}.'
    MOVIE_FILTER_RATING = 'Enter minimum rating (leave blank for no minimum rating): '
    MOVIE_FILTER_START_YEAR = 'Enter start year (leave blank for no start year): '
    MOVIE_FILTER_END_YEAR = 'Enter end year (leave blank for no end year): '
    MOVIE_FILTER_NO_RESULT = 'No Movies found for this filter set.'
    MOVIE_DATA_SAVED = 'Movie data successfully saved.'
    GENERAL_ERROR = 'An unexpected error occurred: {error}'
    GENERAL_EMPTY_ERROR = '{KEY} cannot be empty.'
    GENERAL_MENU_CMD = '[Enter empty text for Menu.]'

    # File error
    FILE_NOT_EXIST = 'File does not exist on Path {KEY}'
