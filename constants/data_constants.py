"""The JsonConstants Module."""


class DataConstants:
    """The JsonConstants Class."""
    __id = "id"
    __title = "title"
    __rating = "rating"
    __year = "year"
    __poster = "poster"
    __country = "country"
    __notes = "notes"

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
        """Method to get the Release Year Key."""
        return cls.__poster

    @classmethod
    def country(cls):
        """Method to get the Country Key."""
        return cls.__country

    @classmethod
    def notes(cls):
        """Method to get the notes Key."""
        return cls.__notes
