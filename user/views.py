import logging
import json

from flask import request
from flask.blueprints import Blueprint
from util.api import APIResult, api_wrap 
from .user_service import User_Service
from .json_to_dict import JsonObject

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

@leyouv_users.route('/pauli',methods=['POST'])
@api_wrap
def init_session_key():
    try:
        content = json.loads(request.data.decode("utf-8"), object_hook=JsonObject)
        session_key=User_Service.get_user_session_key(content)
        return APIResult(0,session_key)
    except Exception as ex:
        logging.error('init_session_key error>>%s' % ex)
        return APIResult(201,'error')

@leyouv_users.route('/certify/<waypointid>/<sessionid>',methods=['GET'])
@api_wrap
def certify_user_sessionid(waypointid,sessionid):
    try:
        data=User_Service.get_user_by_sessionid(waypointid,sessionid)
        return  APIResult(0,data)

    except Exception as ex:
        logger.error("certify_user_sessionid error=>> %s" % ex)
        return  APIResult(201,'error')

@leyouv_users.route('/addcommnet',methods=['POST'])
@api_wrap
def add_user_commnet():
    try:
        content = json.loads(request.data.decode("utf-8"), object_hook=JsonObject)
        print(request.data)
        result=User_Service.add_user_comment(content)
        if result:
            return APIResult(0)
        else:
            return APIResult(-1,'error')
    except Exception as ex:
        logger.error("add_user_commnet error=>> %s" % ex)
        return  APIResult(201,'error');