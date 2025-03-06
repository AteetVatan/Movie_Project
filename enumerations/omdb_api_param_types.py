"""Enumeration for OMDB API"""
from enum import Enum
from config import config


class OMDBApiParamTypes(Enum):
    """The OMDB API Query parameters Enumeration."""
    TITLE = config.OMDB_API_QUERY_TITLE_PARAM_NAME
    ID = config.OMDB_API_QUERY_ID_PARAM_NAME
    TYPE = config.OMDB_API_QUERY_TYPE_PARAM_NAME
    SEARCH = config.OMDB_API_QUERY_SEARCH_PARAM_NAME
