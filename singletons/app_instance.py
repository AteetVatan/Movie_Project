# app_instance.py

from .app_factory import create_app

app = None  # this will hold the singleton app instance

def get_app():
    global app
    if not app:
        app = create_app()
    return app
