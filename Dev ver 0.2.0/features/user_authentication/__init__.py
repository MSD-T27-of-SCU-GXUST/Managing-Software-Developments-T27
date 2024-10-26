from flask import Blueprint

user_authentication_bp = Blueprint('user_authentication', __name__)

from . import routes
