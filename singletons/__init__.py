"""Module for singletons."""
from .db_instance import DbInstance
from .app_instance import AppInstance

__all__ = ["DbInstance", "AppInstance"]
