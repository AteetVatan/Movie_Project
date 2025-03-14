"""Module for IStorage interface"""
from abc import ABC, abstractmethod


class IStorage(ABC):
    """IStorage interface"""

    @abstractmethod
    def list_movies(self):
        """abstractmethod to list_movies"""
        return

    @abstractmethod
    def add_movie(self):
        """abstractmethod to add_movie"""
        return

    @abstractmethod
    def delete_movie(self):
        """abstractmethod to delete_movie"""
        return

    @abstractmethod
    def update_movie(self):
        """abstractmethod to update_movie"""
        return
