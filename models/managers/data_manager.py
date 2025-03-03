"""Module for Data utility methods."""


class DataManager:
    """Data operations class."""

    @staticmethod
    def data_by_key(data, key) -> list:
        """Return the list of given key."""

        def key_check(x):
            return x.lower() if isinstance(x, str) else x

        return [key_check(x[key]) for x in data.values()]

    @staticmethod
    def data_by_keys(data, *keys) -> list[tuple]:
        """Return the tuple list of given keys."""
        combined_list = []
        for key in keys:
            combined_list.append(DataManager.data_by_key(data, key))
        combined_list = list(zip(*combined_list))
        return list(combined_list)

    @staticmethod
    def data_key_by_kv(data, unique_key, value) -> int:
        """Return the key of item with a given key and value pair."""
        item = [(x, y) for x, y in data.items() if y[unique_key].lower() == value.lower()]
        return item[0][0]

    @staticmethod
    def base_add_data_operation(data, **kwargs):
        """Adds the new data."""
        item = {**kwargs}  # {"title": "12 Angry Men","rating": 9.5,"year": 2010}
        length = len(data)
        data[length + 1] = item
        return data

    @staticmethod
    def base_update_data_operation(data, unique_key, **kwargs):
        """Adds the new data."""
        item = {**kwargs}  # {"title": "12 Angry Men","rating": 9.5}
        item_key = DataManager.data_key_by_kv(data, unique_key, item[unique_key])
        for key, value in kwargs.items():
            data[item_key][key] = value
        return data

    @staticmethod
    def base_delete_data_operation(data, key, value):
        """Method to delete data."""
        item_key = DataManager.data_key_by_kv(data, key, value)
        del data[item_key]
        return data
