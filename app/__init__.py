# A webapp to share files
# 
# Author: Indrajit Ghosh
# Created On: Mar 05, 2024
# 

from flask import Flask
import logging
from config import get_config, LOG_FILE

def configure_logging(app:Flask):
    logging.basicConfig(
        format='[%(asctime)s] %(levelname)s %(name)s: %(message)s',
        filename=str(LOG_FILE)
    )

    if app.debug:
        logging.getLogger().setLevel(logging.DEBUG)
        
        # Fix werkzeug handler in debug mode
        logging.getLogger('werkzeug').handlers = []


def create_app(config_class=get_config()):
    """
    Creates an app with specific config class
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Configure logging
    configure_logging(app)

    from app.main import main_bp
    app.register_blueprint(main_bp)

    from app.api import api_bp
    app.register_blueprint(api_bp)

    @app.route('/test/')
    def test():
        return '<h1>Testing the Flask Application ShareHub!</h1>'

    return app