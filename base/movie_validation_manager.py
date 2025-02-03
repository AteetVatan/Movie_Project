"""Module for Movies data Validation methods."""
from datetime import datetime
from helpers.movie_print import MoviePrint as Mp, MoviePrintEnum as Me


class MovieValidationManager:
    """Class for Movies data Validation methods."""

    @staticmethod
    def rating_validation(rating):
        """User Entered Rating Validation Method."""
        if rating:
            try:
                rating = float(rating)
                if not 1 <= rating <= 10:
                    Mp.pr_error(Mp.get_prompt_string(Me.MOVIE_RATING_MSG.value))
                    return False
            except ValueError:
                Mp.pr_error(Mp.get_prompt_string(Me.MOVIE_RATING_MSG.value))
                return False
        return True

    @staticmethod
    def year_validation(year):
        """User Entered Year Validation Method."""
        if year:
            current_year = datetime.now().year
            try:
                year = int(year)
                if not 1900 <= year <= current_year:
                    Mp.pr_error(Mp.get_prompt_string(Me.MOVIE_YEAR_PROMPT_ERROR.value,
                                                     KEY1=current_year))
                    return False
            except ValueError:
                Mp.pr_error(Mp.get_prompt_string(Me.MOVIE_YEAR_PROMPT_ERROR.value,
                                                 KEY1=current_year))
        return True
