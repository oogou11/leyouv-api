import logging
import json

from flask import request
from flask.blueprints import Blueprint
from util.api import APIResult, api_wrap 
from .user_service import User_Service

leyouv_users = Blueprint("leyouv_users", __name__)
logger = logging.getLogger('users')

@leyouv_users.route('/<userid>',methods=['GET'])
@api_wrap
def get_user_id(userid):
    try:
        result=User_Service.get_user_by_id(userid)
        return APIResult(0,result)
    except Exception as ex:
        logger.error('users get_user_id error>> %s',ex)
        return APIResult(211,'error')

@leyouv_users.route('/login',methods=['POST'])
@api_wrap
def init_user_info():
     json_data=json.loads(request.data)

@leyouv_users.route('/pauli/sessionkey',methods=['GET'])
@api_wrap
def init_session_key(sessionkey):
    pass