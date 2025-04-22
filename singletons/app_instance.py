"""The App instance Module"""

from .app_factory import create_app

APP = None  # this will hold the singleton app instance


class AppInstance:
    """The Singleton Flask Appinstance class."""
    _app_instance = None

    @classmethod
    def get_app(cls):
        """Method for singleton app instance"""
        if not cls._app_instance:
            cls._app_instance = create_app()
        return cls._app_instance
