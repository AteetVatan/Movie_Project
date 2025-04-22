"""The Main Flask Movie App Module."""
from helpers import PortHelper
from controllers import MovieFlaskController
from singletons import AppInstance

if __name__ == '__main__':
    PORT = 5001
    port_helper = PortHelper()
    port_helper.check_port(PORT)
    APP = AppInstance.get_app()
    with APP.app_context():
        movie_flask_controller = MovieFlaskController(APP)
    APP.run(host="0.0.0.0", port=PORT, debug=True, use_reloader=False)
