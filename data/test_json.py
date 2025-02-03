"""Module to test the Json data"""
from os import getcwd
from data_handler import DataHandler
from constants.json_constants import JsonConstants



def test_json_keys():
    """Function to test Json keys in data are same as systen Json keys"""
    # get json keys set defined in system
    json_keys_set = set(entity for entity in dir(JsonConstants) if not entity.startswith("_"))
    # get json keys set from the given json file
    json_dict = DataHandler.read_data(getcwd() + "\\" + DataHandler.json_file_name())
    first_dict_item_keys_set = set(((list(json_dict.values()))[0]).keys())
    # key sets difference
    keys_set_difference = first_dict_item_keys_set.difference(json_keys_set)
    # keys_set_difference length > 0 if there is key mismatch
    assert len(keys_set_difference) == 0, \
        "Json key mismatch :Json data system keys does not match with given Json data keys"
