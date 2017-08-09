from flask import request
from flask.blueprints import Blueprint
from util.api import APIResult, api_wrap 
from .user_service import User_Service
import logging

leyouv_users = Blueprint("leyouv_users", __name__)
logger = logging.getLogger('users')

@leyouv_users.route('/users/<userid>',methods=['GET'])
@api_wrap
def get_user_id(userid):
    try:
        result=User_Service.get_user_by_id(userid)
        return APIResult(0,result)
    except Exception as ex:
        logger.error('users get_user_id error>> %s',ex)
        return APIResult(211,'error')