"""The JsonConstants Module."""


class DataConstants:
    """The JsonConstants Class."""
    __id = "id"
    __imdb_id = "imdb_id"
    __title = "title"
    __rating = "rating"
    __year = "year"
    __director = "director"
    __actors = "actors"
    __writer = "writer"
    __genre = "genre"
    __plot = "plot"
    __language = "language"
    __awards = "awards"
    __poster = "poster"
    __country = "country"
    __notes = "notes"

    @classmethod
    def id(cls):
        """Method to get the Title Key."""
        return cls.__id

    @classmethod
    def imdb_id(cls):
        """Method to get the IMDB ID Key."""
        return cls.__imdb_id

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
    def notes(cls):
        """Method to get the notes Key."""
        return cls.__notes
