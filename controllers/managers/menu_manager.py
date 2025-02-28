"""Module for Menu utility methods."""
class MenuManager:
    """Menu operations class."""

    def __init__(self, menu_items):
        self.__menu_items = menu_items

    def get_menu_method_by_index(self, index):
        """Property to retrieve the user operation method."""
        return self.__menu_items[index]["method"]

    def get_menu_arguments_by_index(self, index):
        """Property to retrieve the user operation method Arguments."""
        if "kwargs" in self.__menu_items[index].keys():
            return self.__menu_items[index]["kwargs"]
        return {}
