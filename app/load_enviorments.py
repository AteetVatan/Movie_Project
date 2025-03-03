"""Module to load the environment parameters."""
import os
from dotenv import load_dotenv


class LoadEnvironment:
    """Class to load the environment parameters."""
    __ENV_OMDB_API_KEY_ID = "OMDB_API_KEY_NAME"
    __ENV_OMDB_API_VALUE_ID = "OMDB_API_KEY_VALUE"
    __omdb_api_key_name = ""
    __omdb_api_key_value = ""

    def __init__(self):
        load_dotenv()
        self.load_animals_api_environment()

    @property
    def omdb_api_key_name(self):
        """Animal API Key"""
        return self.__omdb_api_key_name

    @property
    def omdb_api_key_value(self):
        """Animal API Key Value"""
        return self.__omdb_api_key_value

    def load_omdb_api_environment(self):
        """Method to Load Environment Variables"""
        self.__omdb_api_key_name = os.getenv(self.__ENV_OMDB_API_KEY_ID)
        self.__omdb_api_key_value = os.getenv(self.__ENV_OMDB_API_VALUE_ID)
