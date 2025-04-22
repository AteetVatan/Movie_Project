""" The App Factory Module."""

import os
from flask import Flask
from config import config
from .db_instance import DbInstance


def create_app():
    """Create and configure the Flask application."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    app = Flask(
        __name__,
        static_folder=os.path.join(base_dir, 'static'),
        template_folder=os.path.join(base_dir, 'templates')
    )

    # Ensure data directory exists
    data_dir = os.path.join(os.getcwd(), config.DB_DIRECTORY)
    os.makedirs(data_dir, exist_ok=True)

    # Path setup for SQLite DB
    db_path = os.path.join(os.getcwd(), config.DB_DIRECTORY, config.DB_NAME)
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    # Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI.format(db_path=db_path)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

    # Initialize extensions
    db = DbInstance.get_db()
    db.init_app(app)

    # Register Blueprints if any (optional)
    # from controllers.movies_controller import movies_bp
    # app.register_blueprint(movies_bp)

    return app
