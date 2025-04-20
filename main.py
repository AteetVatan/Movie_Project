from helpers import PortHelper
from controllers import MovieFlaskController
from singletons.app_instance import get_app



if __name__ == '__main__':    
    PORT = 5001
    port_helper = PortHelper()
    port_helper.check_port(PORT)
    app = get_app()
    with app.app_context():
        movie_flask_controller = MovieFlaskController(app)
    app.run(host="0.0.0.0", port=PORT, debug=True, use_reloader=False)
    
    