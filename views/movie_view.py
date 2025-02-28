"""The MovieView Module."""
from helpers import PrintInputHelper as Ph
from constants import ConstantStrings as Cs
from constants.json_constants import JsonConstants as Jc


class MovieView:
    """The MovieView Class."""

    # region CREATE
    @staticmethod
    def data_added(new_movie: str):
        """Method to add data."""
        Ph.pr_menu(Cs.MOVIE_ADDED.format(KEY1=new_movie))

    # endregion CREATE

    # region READ
    @staticmethod
    def movie_list_data(data):
        """Method to list Movie data."""
        movie_length = len(data) + 1
        Ph.pr_bold(Cs.MOVIE_TOTAL.format(KEY1=movie_length))
        for item in data.values():
            title = item[Jc.title()]
            release_year = item[Jc.release_year()]
            rating = float(item[Jc.rating()])
            Ph.pr_menu(f"\t{title} ({release_year}): {rating:.2f}")

    @staticmethod
    def random_movie(random_movie_data):
        """Prints random Movies."""
        title = random_movie_data[Jc.title()]
        rating = float(random_movie_data[Jc.rating()])
        Ph.pr_menu(
            (Cs.MOVIE_CHOSEN.format(KEY1=title,
                                    KEY2=f"{rating:.2f}")))

    @staticmethod
    def display_search_data(search_result: list):
        """Prints searched Result."""
        for item in search_result:
            Ph.pr_menu(f"{item[0].title()}, {item[1]}")

    @staticmethod
    def display_sorted_data(sorted_list: list):
        """Prints searched Result."""
        for item in sorted_list:
            Ph.pr_menu(f"{item[0]}: {item[1]}")

    @staticmethod
    def display_filtered_data(filtered_data: list):
        """Prints filtered Result."""
        for item in filtered_data:
            Ph.pr_menu(f"\t{item[0]} ({item[2]}): {item[1]}")

    @staticmethod
    def display_data_stats(best_movies: list,
                           worst_movies: list,
                           avg_rating: float,
                           median_rating: float):
        """Prints data statistics."""
        Ph.pr_menu(Cs.AVG_RATING.format(KEY1=f"{avg_rating:.2f}"))
        Ph.pr_menu(Cs.MEDIAN_RATING.format(KEY1=f"{median_rating:.2f}"))
        for item in best_movies:
            Ph.pr_menu(Cs.MOVIE_BEST.format(
                KEY1=item[Jc.title()], KEY2=item[Jc.rating()]))
        for item in worst_movies:
            Ph.pr_menu(Cs.MOVIE_WORST.format(
                KEY1=item[Jc.title()], KEY2=item[Jc.rating()]))

    # endregion READ

    # region UPDATE
    @staticmethod
    def update_movie_complete(update_movie_name):
        """Prints update_movie_complete success."""
        Ph.pr_menu(Cs.MOVIE_UPDATED.format(KEY1=update_movie_name))

    @staticmethod
    def save_movie_data_complete():
        """Prints save data success."""
        Ph.pr_menu(Cs.MOVIE_DATA_SAVED)

    # endregion UPDATE

    # region DELETE
    @staticmethod
    def movie_delete_operation(movie_name: str, success: bool):
        """View method to show delete operation method output."""
        if success:
            Ph.pr_menu(Cs.MOVIE_DELETE_DONE.format(KEY1=movie_name))
        else:
            Ph.pr_error(Cs.MOVIE_NOT_EXIST.format(KEY1=movie_name))

    # endregion DELETE

    @staticmethod
    def movie_error(error: str):
        """View method to show error."""
        Ph.pr_error(error)

    @staticmethod
    def movie_msg(mgg: str):
        """View method to show a message."""
        Ph.pr_bold(mgg)
