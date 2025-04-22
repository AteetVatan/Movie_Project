"""Module for database models."""
from .users import Users
from .movies import Movies
from .user_movies import UserMovies

__all__ = ["Users", "Movies", "UserMovies"]
