from flask import request
from flask.blueprints import Blueprint
from util.api import APIResult,api_wrap
from .user_service import User_Service
import logging

leyouv_users = Blueprint("leyouv_users", __name__)
logger = logging.getLogger('users')

@leyouv_users.route('/leyouv/users',methods=['GET'])
@api_wrap
def get_uses_by_id():
    return ''