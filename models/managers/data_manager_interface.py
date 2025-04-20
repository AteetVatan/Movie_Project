from abc import ABC, abstractmethod

class DataManagerInterface(ABC):
    """Interface to abstract data layer between File/DB implementations."""

    # region READ
    @abstractmethod
    def read_data(self, **kwargs):
        """Read all movie data from the storage."""
        pass
    
    @abstractmethod
    def get_all_users(self):
        """Get all users from the storage."""
        pass

    @abstractmethod
    def get_user_movies(self, user_id):
        """Get all movies associated with a specific user."""
        pass
    # endregion

    # region CREATE
    @abstractmethod
    def add_movie(self, **kwargs):
        """Add a new movie to the storage."""
        pass
    # endregion

    # region UPDATE
    @abstractmethod
    def update_movie(self, **kwargs):
        """Update an existing movie in the storage."""
        pass

    @abstractmethod
    def write_data(self, **kwargs):
        """Write movie data to the storage."""
        pass
    # endregion

    # region DELETE
    @abstractmethod
    def delete_movie(self, title):
        """Delete a movie from the storage."""
        pass
    # endregion
