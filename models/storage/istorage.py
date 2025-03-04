"""Module for IStorage interface"""
from abc import ABC, abstractmethod


class IStorage(ABC):
    """IStorage interface"""

    @abstractmethod
    def list_movies(self):
        """abstractmethod to list_movies"""
        return

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """abstractmethod to add_movie"""
        return

    @abstractmethod
    def delete_movie(self, title):
        """abstractmethod to delete_movie"""
        return

    @abstractmethod
    def update_movie(self, title, rating):
        """abstractmethod to update_movie"""
        return
