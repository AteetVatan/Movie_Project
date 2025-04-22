"""The JsonConstants Module."""
from .data_constants import DataConstants


class OmdbConstants:
    """The JsonConstants Class."""
    __id = "imdbID"
    __title = "Title"
    __rating = "imdbRating"
    __year = "Year"
    __director = "Director"
    __actors = "Actors"
    __writer = "Writer"
    __genre = "Genre"
    __plot = "Plot"
    __language = "Language"
    __awards = "Awards"
    __poster = "Poster"
    __country = "Country"
    __response = "Response"

    __omdb_data_mapping = {__id: DataConstants.id(),
                           __title: DataConstants.title(),
                           __rating: DataConstants.rating(),
                           __year: DataConstants.year(),
                           __poster: DataConstants.poster(),
                           __country: DataConstants.country(),
                           __director: DataConstants.director(),
                           __actors: DataConstants.actors(),
                           __writer: DataConstants.writer(),
                           __genre: DataConstants.genre(),
                           __plot: DataConstants.plot(),
                           __language: DataConstants.language(),
                           __awards: DataConstants.awards()}

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
    def director(cls):
        """Method to get the Director Key."""
        return cls.__director

    @classmethod
    def actors(cls):
        """Method to get the Actors Key."""
        return cls.__actors

    @classmethod
    def writer(cls):
        """Method to get the Writer Key."""
        return cls.__writer

    @classmethod
    def genre(cls):
        """Method to get the Genre Key."""
        return cls.__genre

    @classmethod
    def plot(cls):
        """Method to get the Plot Key."""
        return cls.__plot

    @classmethod
    def language(cls):
        """Method to get the Language Key."""
        return cls.__language

    @classmethod
    def awards(cls):
        """Method to get the Awards Key."""
        return cls.__awards

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
