# A webapp to share files
# Author: Indrajit Ghosh
# Created On: Mar 05, 2024

from flask import Flask
from config import get_config

def create_app(config_class=get_config()):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.main import main_bp
    app.register_blueprint(main_bp)

    from app.api import api_bp
    app.register_blueprint(api_bp)

    return app