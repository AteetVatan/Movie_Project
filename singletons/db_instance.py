"""Module for singleton db instance."""

from flask_sqlalchemy import SQLAlchemy


class DbInstance:
    """Class for singleton database instance"""
    _db_instance = None

    @classmethod
    def get_db(cls):
        """Method to get singleton dn instance."""
        if not cls._db_instance:
            cls._db_instance = SQLAlchemy()
        return cls._db_instance
