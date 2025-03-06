"""The JsonConstants Module."""
from constants.data_constants import DataConstants


class OmdbConstants:
    """The JsonConstants Class."""
    __id = "imdbID"
    __title = "Title"
    __rating = "imdbRating"
    __year = "Year"
    __poster = "Poster"
    __country = "Country"
    __response = "Response"

    __omdb_data_mapping = {__id: DataConstants.id(),
                           __title: DataConstants.title(),
                           __rating: DataConstants.rating(),
                           __year: DataConstants.year(),
                           __poster: DataConstants.poster()}

    @classmethod
    def get_data_constant_key(cls, omdb_key):
        """Method get the corresponding mapped DataConstants key."""
        return cls.__omdb_data_mapping.get(omdb_key)

    @classmethod
    def id(cls):
        """Method to get the Title Key."""
        return cls.__id

    @classmethod
    def title(cls):
        """Method to get the Title Key."""
        return cls.__title

    @classmethod
    def rating(cls):
        """Method to get the Rating Key."""
        return cls.__rating

    @classmethod
    def year(cls):
        """Method to get the Release Year Key."""
        return cls.__year

    @classmethod
    def poster(cls):
        """Method to get the Poster Key."""
        return cls.__poster

    @classmethod
    def country(cls):
        """Method to get the Country Key."""
        return cls.__country

    @classmethod
    def response(cls):
        """Method to get the Release Year Key."""
        return cls.__response

    @classmethod
    def item_found(cls, response):
        """Method to check the response variable is True."""
        return response.get(cls.__response, "").lower() == 'true'
