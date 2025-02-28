"""The JsonConstants Module."""
class JsonConstants:
    """The JsonConstants Class."""
    __title = "title"
    __rating = "rating"
    __release_year = "release_year"

    @classmethod
    def title(cls):
        """Method to get the Title Key."""
        return cls.__title

    @classmethod
    def rating(cls):
        """Method to get the Rating Key."""
        return cls.__rating

    @classmethod
    def release_year(cls):
        """Method to get the Release Year Key."""
        return cls.__release_year
