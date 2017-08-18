import logging
from flask import request
from flask.blueprints import Blueprint
from util.api import APIResult, api_wrap

leyouv_schedule = Blueprint("leyouv_schedule", __name__)
logger = logging.getLogger('schedule')

@leyouv_schedule.route('/list', methods=['GET'])
@api_wrap
def get_schedule_list():
    data={
        "data":[{
            "name":"test"
        }],
        "nextStart":5
    }
    return APIResult(0,data)