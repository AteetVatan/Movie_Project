"""Module for Data utility methods."""


class DataManager:
    """Data operations class."""

    def __init__(self, data):
        self.__data = data

    def data_by_key(self, key) -> list:
        """Return the list of given key."""

        def key_check(x):
            return x.lower() if isinstance(x, str) else x

        return [key_check(x[key]) for x in self.__data.values()]

    def data_by_keys(self, *keys) -> list[tuple]:
        """Return the tuple list of given keys."""
        combined_list = []
        for key in keys:
            combined_list.append(self.data_by_key(key))
        combined_list = list(zip(*combined_list))
        return list(combined_list)

    def data_key_by_kv(self, unique_key, value) -> int:
        """Return the key of item with given key and value pair."""
        item = [(x, y) for x, y in self.__data.items() if y[unique_key].lower() == value.lower()]
        return item[0][0]

    def base_add_data_operation(self, **kwargs) -> None:
        """Adds the new data."""
        item = {**kwargs}  # {"title": "12 Angry Men","rating": 9.5,"release_year": 2010}
        length = len(self.__data)
        self.__data[length + 1] = item

    def base_update_data_operation(self, unique_key, **kwargs) -> None:
        """Adds the new data."""
        item = {**kwargs}  # {"title": "12 Angry Men","rating": 9.5}
        item_key = self.data_key_by_kv(unique_key, item[unique_key])
        for key, value in kwargs.items():
            self.__data[item_key][key] = value

    def base_delete_data_operation(self, key, value) -> None:
        """Method to delete data."""
        item_key = self.data_key_by_kv(key, value)
        del self.__data[item_key]
