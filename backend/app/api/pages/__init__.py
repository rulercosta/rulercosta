"""
Pages API initialization
"""
from flask import Blueprint

bp = Blueprint('pages', __name__)

from . import routes
