from flask import request
from flask.blueprints import Blueprint
from util.api import APIResult, api_wrap 
import logging

leyouv_users = Blueprint("leyouv_users", __name__)
logger = logging.getLogger('users')

@leyouv_users.route('/users/<userid>',methods=['GET'])
@api_wrap
def get_user_id(userid):
    
    return APIResult(0,'')