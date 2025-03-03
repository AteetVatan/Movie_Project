"""The JsonConstants Module."""
class DataConstants:
    """The JsonConstants Class."""
    __index = "index"
    __title = "title"
    __rating = "rating"
    __year = "year"
    __image = ""

    @classmethod
    def index(cls):
        """Method to get the Title Key."""
        return cls.__index

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
    def image(cls):
        """Method to get the Release Year Key."""
        return cls.__image
