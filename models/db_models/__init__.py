# Import models after db is defined to avoid circular imports
from .users import Users
from .movies import Movies
from .user_movies import UserMovies

__all__ = ["Users", "Movies", "UserMovies"]
