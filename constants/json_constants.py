class JsonConstants:
    __title = "title"
    __rating = "rating"
    __release_year = "release_year"

    @classmethod
    def title(cls):
        return cls.__title

    @classmethod
    def rating(cls):
        return cls.__rating

    @classmethod
    def release_year(cls):
        return cls.__release_year
