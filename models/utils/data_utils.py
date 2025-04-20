"""Module for Data utility methods."""


class DataUtils:
    """Data Utils class."""

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
            combined_list.append(DataUtils.data_by_key(data, key))
        combined_list = list(zip(*combined_list))
        return list(combined_list)

    @staticmethod
    def data_key_by_kv(data, unique_key, value) -> int:
        """Return the key of item with a given key and value pair."""
        item = [(x, y) for x, y in data.items() if y[unique_key].lower() == value.lower()]
        return item[0][0]
