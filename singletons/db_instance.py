# db_instance.py

from flask_sqlalchemy import SQLAlchemy

_db_instance = None

def get_db():
    global _db_instance
    if not _db_instance:
        _db_instance = SQLAlchemy()
    return _db_instance
