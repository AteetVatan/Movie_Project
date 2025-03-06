""" Module for API Request Model."""
from config import config
from config.load_enviorments import LoadEnvironment
from enumerations import OMDBApiParamTypes


class ApiRequestModel:
    """ Class for API Request Model."""
    __api_base_url = __key_name = __key_value = ""
    __query_endpoint = ""

    def __init__(self):
        env = LoadEnvironment()
        self.__api_base_url = config.OMDB_API_BASE_URL
        self.__key_name = env.omdb_api_key_name
        self.__key_value = env.omdb_api_key_value
        self.__query_endpoint = config.OMDB_API_QUERY_ENDPOINT
        self.__query_param_title_key = config.OMDB_API_QUERY_TITLE_PARAM_NAME

    @property
    def endpoint_url(self):
        """ Method to get endpoint_url."""
        return f"{self.__api_base_url}{self.__query_endpoint}"

    @property
    def header_dict(self):
        """ Method to get the HTTP get request header dictionary."""
        return {self.__key_name: self.__key_value}

    @property
    def api_base_url(self):
        """ Method to api base URL."""
        return self.__api_base_url

    @property
    def key_name(self):
        """ Method to API Key Name in a config file."""
        return self.__key_name

    @property
    def key_value(self):
        """ Method to API Key Value Name in config file."""
        return self.__key_value

    def get_query_string(self, param_type: OMDBApiParamTypes, param_value):
        """ Method to get the Http request Query end point."""
        return f"?{self.__key_name}={self.__key_value}&{param_type.value}={param_value}"

    @property
    def query_endpoint(self):
        """ Method to get the Http request Query end point."""
        return self.__query_endpoint

    @property
    def query_param_title_key(self):
        """ Method to get query_param_key."""
        return self.__query_param_title_key
