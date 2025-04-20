"""Module providing interface functionality and abstract CRUD methods which must be implemented on
Inheritance."""
from abc import ABC, abstractmethod
from controllers.managers import MenuManager


class BaseController(ABC):
    """Base class interface will abstract methods."""

    def __init__(self, menu_items: dict):
        self.__menu_items = menu_items
        self.menu_manager = MenuManager(menu_items)

    @property
    def get_menu_items(self):
        """Property giving dictionary of menu items."""
        return self.__menu_items

    @property
    def get_menu_items_descriptions(self):
        """Property giving menu items."""
        return [x["desc"] for x in self.__menu_items.values()]

    @property
    def get_menu_items_length(self):
        """Property for User menu Length."""
        return len(self.__menu_items)

    # region CREATE
    @abstractmethod
    def add_data(self) -> bool:
        """Abstract method to add data."""
        return False

    # endregion CREATE

    # region READ
    @abstractmethod
    def list_data(self) -> bool:
        """Abstract method to list data."""
        return False

    @abstractmethod
    def show_random_item_in_data(self) -> bool:
        """Abstract method to show random item in data."""
        return False

    @abstractmethod
    def search_data(self) -> bool:
        """Abstract method to search data."""
        return False

    @abstractmethod
    def sort_data(self, key, reverse=False) -> bool:
        """Abstract method to Sort data by given key."""
        return False

    @abstractmethod
    def data_stats(self) -> bool:
        """Abstract method for data stat."""
        return False

    @abstractmethod
    def data_filter(self) -> bool:
        """Abstract method for data filter."""
        return False

    @abstractmethod
    def generate_website(self) -> bool:
        """Abstract method to delete item in data."""
        return False

    # endregion READ

    # region UPDATE
    @abstractmethod
    def update_data(self) -> bool:
        """Abstract method to update data."""
        return False

    @abstractmethod
    def show_data_histogram(self) -> bool:
        """Abstract method to show histogram for data."""
        return False

    # endregion UPDATE

    # region DELETE
    @abstractmethod
    def delete_data(self) -> bool:
        """Abstract method to delete item in data."""
        return False

    @abstractmethod
    def save_data(self) -> bool:
        """Abstract method to delete item in data."""
        return False

    # endregion DELETE

    # region EXIT
    @abstractmethod
    def exit(self) -> bool:
        """Abstract method to exit the run time environment."""
        return False

    # endregion EXIT
