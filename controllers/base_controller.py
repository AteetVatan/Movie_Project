"""Module providing interface functionality and abstract CRUD methods which must be implemented on
Inheritance."""
from abc import ABC, abstractmethod

from controllers.managers import MenuManager
from constants.data_constants import DataConstants as Jc


class BaseController(ABC):
    """Base class interface will abstract methods."""

    def __init__(self, data_desc: str):
        self.__menu_items = self.__get_menu_dictionary(data_desc)
        self.menu_manager = MenuManager(self.__menu_items)

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

    # region private-methods
    def __get_menu_dictionary(self, data_desc) -> dict:
        return {
            1: {"method": self.exit, "desc": "Exit".title()},
            2: {"method": self.list_data, "desc": f"List {data_desc}s".title()},
            3: {"method": self.add_data, "desc": f"Add {data_desc}".title()},
            4: {"method": self.delete_data, "desc": f"Delete {data_desc}".title()},
            5: {"method": self.update_data, "desc": f"Update {data_desc}".title()},
            6: {"method": self.data_stats, "desc": "Stats".title()},
            7: {"method": self.show_random_item_in_data, "desc": f"Random {data_desc}".title()},
            8: {"method": self.search_data, "desc": f"Search {data_desc}".title()},
            9: {"method": self.sort_data, "kwargs": {"key": Jc.rating()},
                "desc": f"{data_desc}s sorted by {Jc.rating()}".title()},
            10: {"method": self.sort_data, "kwargs": {"key": Jc.year()},
                 "desc": f"{data_desc}s sorted by {Jc.year()}".title()},
            11: {"method": self.data_filter, "desc": f"filter {data_desc}".title()},
            12: {"method": self.show_data_histogram,
                 "desc": f"Show {data_desc}s Histogram".title()},
            13: {"method": self.save_data, "desc": "Save".title()}
        }
    # endregion private-methods
