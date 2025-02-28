"""Module to test the JSON data"""
from os import getcwd
from models import FileHandlerModel
from constants.json_constants import JsonConstants



def test_json_keys():
    """Function to test JSON keys in data is the same as system JSON keys"""
    # get JSON keys set defined in a system
    json_keys_set = set(entity for entity in dir(JsonConstants) if not entity.startswith("_"))
    # get JSON keys set from the given JSON file
    json_dict = FileHandlerModel.read_data(getcwd() + "\\" + FileHandlerModel.file_name())
    first_dict_item_keys_set = set(((list(json_dict.values()))[0]).keys())
    # key sets difference
    keys_set_difference = first_dict_item_keys_set.difference(json_keys_set)
    # keys_set_difference length > 0 if there is key mismatch
    assert len(keys_set_difference) == 0, \
        "Json key mismatch :Json data system keys does not match with given Json data keys"
