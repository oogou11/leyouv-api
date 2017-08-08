from flask import request
from flask.blueprints import Blueprint
from util.api import APIResult, api_wrap
from .trip_service import Trip_Service
import logging

leyouv_users = Blueprint("leyouv_users", __name__)
logger = logging.getLogger('users')
