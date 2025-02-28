"""Module for Movies data Validation methods."""
from datetime import datetime
from constants.constant_strings import ConstantStrings as Cs


class MovieValidationManager:
    """Class for Movies data Validation methods."""

    @staticmethod
    def rating_validation(rating):
        """User Entered Rating Validation Method."""
        try:
            if not rating:
                raise ValueError(Cs.GENERAL_EMPTY_ERROR.format(KEY="RATING"))
            try:
                rating = float(rating)
            except ValueError:
                raise ValueError(Cs.MOVIE_RATING_ERROR)
            if not 1 <= rating <= 10:
                raise ValueError(Cs.MOVIE_RATING_MSG)
        except ValueError:
            raise

    @staticmethod
    def year_validation(year):
        """User Entered Year Validation Method."""
        current_year = datetime.now().year
        try:
            if not year:
                raise ValueError(Cs.GENERAL_EMPTY_ERROR.format(KEY="YEAR"))
            try:
                year = int(year)
            except ValueError:
                raise ValueError(Cs.MOVIE_YEAR_PROMPT_ERROR.format(KEY=current_year))
            if not 1900 <= year <= current_year:
                raise ValueError(Cs.MOVIE_YEAR_PROMPT_ERROR.format(KEY=current_year))
        except ValueError:
            raise

    @staticmethod
    def movie_name_validation(movie_name):
        """User Entered Rating Validation Method."""
        try:
            if not movie_name:
                raise ValueError(Cs.GENERAL_EMPTY_ERROR.format(KEY="Movie Name"))
            try:
                str(movie_name)
            except ValueError:
                raise ValueError(Cs.MOVIE_NAME_ERROR)
        except ValueError:
            raise
