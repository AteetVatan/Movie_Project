"""This Module will contain all supported file types."""
from enum import Enum


class FileTypes(Enum):
    """The FileTypes Enum."""
    JSON = "json"
    CSV = "csv"
    UNKNOWN = "unknown"