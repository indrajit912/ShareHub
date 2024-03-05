# api of the webapp
from flask import Blueprint

api_bp = Blueprint(
    'api', 
    __name__,
    template_folder="templates", 
    static_folder="static",
    url_prefix='/api'
)

from app.api import routes